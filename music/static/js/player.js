$(document).ready(function() {



$('.name_song').text($('.name_track:first').text())
$('.name_album').text($('.name_track:first').attr('artist'))

function get_and_set_name_song(){
    var name_song = $('.on').text();
    var name_artist = $('.on').attr('artist');
    $('.name_song').text(name_song);
    $('.name_album').text(name_artist);
}//при запуске плеера, ставляем данные в шапку плеера

function count_track(){
        var s = $('.count');
        for(var i = 0; i != s.length; i++){
            $(s[i]).text(i+1);

        }
    };
count_track()
//следующий трек - предыдущий трек
function next(){
    var a = $('.tracklist').find('.name_track');
    //обрабатываем полученный массив
    for (var i = 0; i < a.length; i++){
        if( $(a[i]).hasClass('on') || $(a[i]).hasClass('pause') ){
            $(a[i+1]).trigger('click');
            break;
        };
    };//end for
};



function back(){ 
    //получаем массив элеметов c селектором .button
    var a = $('.tracklist').find('.name_track');
    //обрабатываем полученный массив
    for (var i = 0; i < a.length; i++){
        if( $(a[i]).hasClass('on') || $(a[i]).hasClass('pause') ){
            $(a[i-1]).trigger('click');
            break;
        };
    };//end for
};
//Преобразование чистого времени в формат
function timeformat(input_int){
        var m = Math.floor(input_int/60);
        var s = Math.floor(input_int - (m*60));
        if (s < 10){
            var s = ('0'+s);
        };
        return (m + ':' + s);
};


///////////////////////////////////////////////////////////////////

    //Стоп-пауза
    var pl = $('#my-player').get(0); //плеер

    $('.name_track').on("click", function(event) {
        //Все управление плеером производится по нажатию на блок с классом name_track
        //кнопки которые затрагивают паузу и стоп ссылаются на этот блок
        //содержащиеся в атрибутах блока данные передаются в плеер

        if ($(this).hasClass('on')) {
            //если данная мелодия уже проигрывается
            //снимаем флаг ON
            $(this).removeClass('on');
            $(this).addClass('pause')

            $('.button').removeClass('go_on');
            //останавливаем проигрыватель
            pl.pause();
        } else if ($(this).hasClass('pause')){
            $(this).removeClass('pause');
            $(this).addClass('on');

            $('.button').addClass('go_on');

            pl.play()

        } else {
            $('.name_track').removeClass('on');
            $('.name_track').removeClass('pause');

            $('.name_track').parent().parent().css('background','');
            $('.name_track').parent().siblings('.arrow').css("background-image","url('')")
            $('.name_track').parent().parent().css('color','white');

            $(this).addClass('on');

            $('.button').addClass('go_on');

            pl.src = $(this).attr('data-src');
            pl.play();    
            get_and_set_name_song();


            $(this).parent().parent().css('background','#605c66');
            $(this).parent().parent().css('color','#d2c293');
            $(this).parent().siblings('.arrow').css("background-image","url('/static/css/images/Strelka.png')")

        }
        event.stopPropagation()
    });


    $('.track_rows').click(function(){
        $(this).find('.name_track').trigger('click');
    });

    //реализация кнопки mute
    $(".button_mut").on("click", function(event){
/*        if ($(this).hasClass('muton')) {
            document.getElementById("my-player").muted = false;
            $(this).removeClass('muton');
        }else{
            $(this).addClass("muton");
            document.getElementById("my-player").muted = true;
        };*/
        
    });
    //обновление полоски прогресса

    //Добавить событие мыиши mousedown на элементе timeupdate! event mousedown
     // переменная ползунка
    var polz = document.getElementById('timeline'); 
    polz.value = 0

    pl.addEventListener('timeupdate', function (event){
        curtime = parseInt(pl.currentTime, 10);

        if( $('#timeline').hasClass('stopUpdateTimeLine') == false ){
            polz.value = curtime;
        }else{
            
            //main функцией timenormal
        };
        $('.realtime').text(timeformat(curtime));
            //если время определено->вывести
        if(isNaN(pl.duration)){
            $('.long').text('0');
        }else{
            $('.long').text(timeformat(pl.duration));
            $('#timeline').attr('max', Math.floor(pl.duration) - 1);

        };
        if((Math.floor(pl.duration)) == curtime){
            next();
        };
    });

    //Переключение момента с помощью ползунка

        $("#timeline").bind("change", function(event) {
                pl.currentTime = $(this).val();
            });

    //Наведение на песню подсветка цветом
    //next track
    $('.next').click(function(){
        //получаем массив элеметов c селектором .button
        next();
    });
    //листать песни назад
        $('.back').click(function(){
            back();
    });

    //при зажатой клавише перестает обнавлятся timeline

    $('#timeline').on('mousedown', function(){
        $(this).addClass('stopUpdateTimeLine')
    });

    $('#timeline').on('mouseup', function(){
        $(this).removeClass('stopUpdateTimeLine')
    });

    //////////////////////////////////////////
    //настройка громкости звука
    var volume = $('#line_volume')
    volume.val(100);
    volume.bind('change', function(event){
        pl.volume = ($(this).val()/100);
        event.stopPropagation();
    });

    volume.on('click', function(event){
        event.stopPropagation();
    }); // no click volume_mute

    //центральная кнопка имитирует нажатие на песню в плейлисте
    $('.button').click(function(){
        if(pl.paused){
            $('.pause').trigger('click');
        }else{
            $('.on').trigger('click');
        };   
        //
        //при первой загрузке кнопка запускает первй трек
        if($('#my-player').attr('src') == undefined){
            $('.name_track:first').trigger('click');
        };

    });

    //Выпадающие меню иконки плейлиста для добавления\удаления\переключения плейлиста



});
