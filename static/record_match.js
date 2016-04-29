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
        var score1 = document.getElementById('numBox1').innerHTML;
        var score2 = document.getElementById('numBox2').innerHTML;

        var player1 = $('#player-1-selector').find("option:selected");
        var player2 = $('#player-2-selector').find("option:selected");

        console.log("data: " + score1 + " " + score2 + " " + player1.data().playerId + " " + player2.data().playerId);

        var data = {'bob': 'foo','paul': 'dog'};
        $.ajax({
            url: "/record_match",
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
            console.log("TEST SINGLES");
        }
    })
});

$(document).ready(function() {
    $("#doubles-btn").click(function() {
        if (mode != DOUBLES) {
            mode = DOUBLES;
            $(this).addClass("active");
            $("#singles-btn").removeClass("active");
            console.log("TEST DOUBLES");
        }
    })
});
