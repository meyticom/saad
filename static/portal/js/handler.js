$(document).ready(function(){
   $('#check-form').click(function(){
       var dataValid = true;
        $('#success').html('');
       $('.required').each(function(){
           var cur = $(this);
           cur.next('span').remove();
           if($.trim(cur.val())== '') {
               cur.after('<span class="error">پر کردن این فیلد الزامی است </span>');
               dataValid = false;
           }
       })
       // if(dataValid)
       //     {
       //         $('#success').html('it is ok');
       //     }
   })
})



