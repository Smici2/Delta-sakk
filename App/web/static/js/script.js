$(document).ready(function()
    {
        var $container = $("#tabla_frissit");
        $container.load("/tabla");
        var refreshId = setInterval(function()
        {
            $container.load('/tabla');
        }, 5000);

        window.mezoValaszt = function(id){ 
            if (seged == 1 && id == idbe) {
                $("#mezo-" + id).css("background-color", "#fff");
                seged = 0;
            }
            if (seged == 0) {
                $("#mezo-" + id).css("background-color", "#bc4749");
                seged = 1;
                idbe = id;
            }
        }

            /*$("#mezo").click(function() {
              //$("#mezo-" + id).css("background-color", "#bc4749");
            console.log($(this).data('id'));
        });*/
    });