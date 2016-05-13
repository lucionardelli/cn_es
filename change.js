$(function(){
    $("td").on('click',function(){
       var c = $(this).attr('class'); 
       if (c.indexOf("change") >= 0){
         return true;
       } else {
         if(confirm("Seguro que elegis la palabra: " + $(this).html() + '?')){
             $(this).removeClass(c);
             $(this).addClass(c+'_change');
         }
       }
    });
});
