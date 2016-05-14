$(function(){
    $("td").on('click',function(){
        $(this).find("span").toggleClass('hide');
    });
});
