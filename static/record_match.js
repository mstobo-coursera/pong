$(document).ready(function(){
    $('.key1').click(function() {
        var numBox = document.getElementById('numBox1');
        onKeyPress(numBox, this);
    });

    $('.key2').click(function() {
        var numBox = document.getElementById('numBox2');
        onKeyPress(numBox, this);
    });
});

function onKeyPress(numBox, key) {
    if (key.innerHTML == "DEL") {
        if (numBox.innerHTML.length > 0) {
            numBox.innerHTML = numBox.innerHTML.substring(0, numBox.innerHTML.length - 1);
        }
    } else if (key.innerHTML == "CLR") {
        numBox.innerHTML = '';
    } else if (key.innerHTML == "0") {
        if (numBox.innerHTML.length > 0) {
	    console.log(key.innerHTML);
            numBox.innerHTML = numBox.innerHTML + key.innerHTML;
        }
    } else {
        numBox.innerHTML = numBox.innerHTML + key.innerHTML;
    }
        
    event.stopPropagation();
}

$(document).ready(function() {
    $('#submit-btn').click(function() {
        var score1 = parseInt(document.getElementById('numBox1').innerHTML);
        var score2 = parseInt(document.getElementById('numBox2').innerHTML);

        var playerId1 = $('#player-1-selector').find("option:selected").data().playerId;
        var playerId2 = $('#player-2-selector').find("option:selected").data().playerId;

        var winner;
        if (score1 > score2) {
            winner = playerId1
        } else {
            winner = playerId2
        }

        var data = { 'user_1': playerId1,
                     'user_2': playerId2,
                     'winner': winner,
                     'user_1_score': score1,
                     'user_2_score': score2
                   };

        $.ajax({
            url: "/match",
            type: 'POST',
            contentType:'application/json',
            data: JSON.stringify(data),
            dataType:'json',
            success: function(data) {
                alert(data);
            },
            error: function(xhr, ajaxOptions, thrownError) {
                if (xhr.status == 200) {
                    alert(ajaxOptions);
                } else {
                    alert(xhr.status);
                    alert(thrownError);
                    }
                }
        });
    });
});

const SINGLES = "singles";
const DOUBLES = "doubles";
$("#singles-btn").addClass("active");
var mode = SINGLES;

$(document).ready(function() {
    $("#singles-btn").click(function() {
        if (mode != SINGLES) {
            mode = SINGLES;
            $(this).addClass("active");
            $("#doubles-btn").removeClass("active");
        }
    })
});

$(document).ready(function() {
    $("#doubles-btn").click(function() {
        if (mode != DOUBLES) {
            mode = DOUBLES;
            $(this).addClass("active");
            $("#singles-btn").removeClass("active");
        }
    })
});
