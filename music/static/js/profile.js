$(document).ready(function() {


///////ЗАПОЛНЕНИЕ И ОТПРАВКА ФОРМЫ ВНЕСЕНИЯ ПЕСНИ В СПИСОК ПЕСЕН\\\\\\\\\
    $('select').hide();

    $('.add_track').click(function(event){

        var select = $('#select_add_song')
        if($(this).children(select).length == 0){
            select.show().appendTo($(this));
        };
        select.show();
        //Заполнения имя песни в форму
        var data_id_track = $(this).attr('id_track');
        $('#id_id_track_model').val(data_id_track);
    });



    //копируем выбор в форму и отправляем-------
    $('option').click(function(){
         //ajax запросы, отправка формы без березагрузки страницы.
        $('#id_title').val($(this).val());
        var formData = $('form').serialize();
        $.post('', formData, function(){
            $('select').hide();
        }); 
    });

////////////////////////////////////////////////////////////////////

    //скрытие элемента по клику в не области кнопки доабвить_песню
    $(document).click(function(event) {
        if ($(event.target).closest(".add_track").length) return;
        $("select").hide("slow");
            event.stopPropagation();
    });

  //УДАЛЯЕМ ПЕСНЮ ИЗ СПИСКА\\\\\\\\\\\\\\\\\\\\
    $('.del_track').click(function(){
        $('#id_id_track').val($(this).attr('id_track'));
        active_pl = $("div[active_pl]").attr('active_pl');
        $('.del #id_title').val(active_pl);
        var form_Data_del = $('.del').serialize();

        $.post('del_song', form_Data_del, function(){
            //Продумать действия после удаления песни
            //Поразмышлять об собтиях в очереди
        }); 

    });
///////////////////////////////////////////////////////


    $('#button_create_pl').click(function(){
        var form_create_data = $('.form_create_playlist').serialize();
        $.post('', form_create_data, function(data, status){
            //Включать новый плейлист в список
        }); 
    });

    $('.button_del_pl').click(function(){
        $('.del_pl #id_title').val($(this).attr('pl'));
        data_del_pl = $('.del_pl').serialize();

        $.post('del_pl',data_del_pl, function(data){
            //Продумать действия после удаления песни
            //Поразмышлять об собтиях в очереди 
        })
    });

});


