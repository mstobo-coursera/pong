$(function(){
    var nameBox = document.getElementById('nameBox'),
        shift = false,
        capslock = false;
     
    $('#keyboard li').click(function(){
        var $this = $(this),
            character = $this.html(); // If it's a lowercase letter, nothing happens to this variable
         
        // Shift keys
        if ($this.hasClass('left-shift') || $this.hasClass('right-shift')) {
            $('.letter').toggleClass('uppercase');
            $('.symbol span').toggle();
             
            shift = (shift === true) ? false : true;
            capslock = false;
            return false;
        }
         
        // Caps lock
        if ($this.hasClass('capslock')) {
            $('.letter').toggleClass('uppercase');
            capslock = true;
            return false;
        }
         
        // Delete
        if ($this.hasClass('delete')) {
            nameBox.innerHTML = nameBox.innerHTML.substr(0, nameBox.innerHTML.length - 1);
            return false;
        }
         
        // Special characters
        if ($this.hasClass('symbol')) character = $('span:visible', $this).html();
        if ($this.hasClass('space')) character = ' ';
        if ($this.hasClass('tab')) character = "\t";


        // Uppercase letter
        if ($this.hasClass('uppercase')) character = character.toUpperCase();
         
        // Remove shift once a key is clicked.
        if (shift === true) {
            $('.symbol span').toggle();
            if (capslock === false) $('.letter').toggleClass('uppercase');
             
            shift = false;
        }

        // Submit
        if ($this.hasClass('submit')) {
            var data = { 'name': nameBox.innerHTML };

            $.ajax({
                url: "/user",
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
            character = "";
        }

        // Add the character
        nameBox.innerHTML = nameBox.innerHTML + character;
    });
});

