$( document ).ready(function() {
    //SHOW ALL THE LIGHTS
    url = "/get-name";
    $.getJSON(url, function(data) {
        $('h1').html('Daft Punk - '+data['data']);
    });

    url = "/list-lights";
    $.getJSON(url, function(data) {
        data = data["data"];


        for (var i = 0; i < data.length; i++) {
            $('.space').append('<div class="light light_'+data[i]["name"]+'" style="top: '+data[i]["y"]+'px; left: '+data[i]["x"]+'px;" onclick="show_light_options(\''+data[i]["name"]+'\');"></div>');
        }
    });
});


function show_light_options(light) {
    console.log(light);

    var content = '<h2>'+light+' options:</h2>';
        content += '<button onclick="light_on(\''+light+'\', true);">On</button>/';
        content += '<button onclick="light_on(\''+light+'\', false);">Off</button><br /><br />';
        content += '<input type="text" class="startEmpty" value="" /><br /><br />';
        content += '<button onclick="hide_options();">Cancel (X)</button><br /><br />';

    $('.space .options').html(content);
    $(".startEmpty").spectrum({
        allowEmpty: true,
        change: function() {
            var t = $(".startEmpty").spectrum("get");
            var c = t.toHex();
            console.log(c);
            colour(light, ""+c);
        }
    });

    $('.options').show();
}


function hide_options() {
    $('.space .options').html('');
    $('.options').hide();
}

function colour(light, c) {
    hide_options();
    console.log(c);

    url = "/colour?light="+light+"&colour=%23"+encodeURI(c);

    console.log(url);
    $('.light_'+light).css('background-color', "#"+c);
    $.getJSON(url, function(data) {
        console.log(data);
    });
}


function light_on(light, on) {
    hide_options();
    var x = "False";
    if (on) {
        x = "True";
    } else {
        $('.light_'+light).css('background-color', "#999999");
    }

    url = "/on?light="+light+"&on="+x;
    $.getJSON(url, function(data) {
        console.log(data);
    });
}
