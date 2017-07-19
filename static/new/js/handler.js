$(document).ready(function(){
   $('#check-form').click(function(){
       var dataValid = true;
       $('.required').each(function(){
           var cur = $(this);
           cur.next('span').remove();
           if($.trim(cur.val())!== '')
                      {
                          $('#send').show();
                      }
           if($.trim(cur.val())== '') {
               cur.after('<span class="error">پر کردن این فیلد الزامی است </span>');
               dataValid = false;

           }
       })

   })
})



