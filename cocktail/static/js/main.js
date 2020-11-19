setTimeout ( function() {
  $('#message').fadeOut('slow');
}, 3000);


// AJAX for posting comment
$('#form-id').on('submit', function(e){
  e.preventDefault();
  console.log("form submitted!") // sanity check
  
  let post_id = $(this).data('id');
 
  $.ajax({
      url : "/post/" + post_id, // the endpoint
      type : "POST", // http method
      data : { 
        post_id: post_id,
        comment: $('#body-id').val() 
      }, // data sent with the post request

      // handle a successful response
      success : function(json) {
          $('#body-id').val(''); // remove the value from the input
          console.log(json); // log the returned json to the console
          const element = document.querySelector('.comments');
          if(element) {
            console.log(element);
            element.innerHTML=`${json}${element.innerHTML}`;
            addCommentLikes();
            addPostLikes()
          }
          console.log("success"); // another sanity check
      },

      // handle a non-successful response
      error : function(xhr) {
          console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
      }
  });
});

const addCommentLikes = () => {
  const likeButtons = document.querySelectorAll('button[data-comment-id]');


  likeButtons.forEach(button => {
    button.addEventListener('click', async () => {
      const { commentId, postId } = button.dataset;
      const reqUrl = `${postId}/comment_like/${commentId}`;
      const res = await fetch(reqUrl);
      const data = await res.json();
      const { isLiked } = data;
      console.log(data);
      
      const likeCountElement = document.querySelector(`#commentlike-${commentId} .like-count`);
      const likeImage = document.querySelector(`#commentlike-${commentId} img`)
      if (!likeCountElement) return;
      const likeCount = Number(likeCountElement.innerText);

      if(isLiked) {
        likeCountElement.innerText = likeCount + 1;
        likeImage.classList.add('bg-likes-after');
      } else {
        likeCountElement.innerText = likeCount - 1;
        likeImage.classList.remove('bg-likes-after');
      }
    })
  });
}

addCommentLikes();


const addPostLikes = () => {
  const likeButton = document.querySelector('button[data-post-id]');
  console.log(likeButton)
  if (likeButton) {
    likeButton.addEventListener('click', async () => {
      const { postId } = likeButton.dataset;
      const reqUrl = `${postId}/post_like`;
      const res = await fetch(reqUrl);
      const data = await res.json();
      const { isLiked } = data;
      console.log(data);
      
      const likeCountElement = document.querySelector(`#postlike-${postId} .like-count`);
      const likeImage = document.querySelector(`#postlike-${postId} img`)


      if (!likeCountElement) return;
      const likeCount = Number(likeCountElement.innerText);

      if(isLiked) {
        likeImage.classList.add('bg-likes-after');
        likeCountElement.innerText = likeCount + 1;
      } else {
        likeImage.classList.remove('bg-likes-after');
        likeCountElement.innerText = likeCount - 1;
      }
    })
  }
}

addPostLikes()



















$(function() {

  // This function gets cookie with a given name
  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');

  /*
  The functions below will create a header with csrftoken
  */

  function csrfSafeMethod(method) {
      // these HTTP methods do not require CSRF protection
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  function sameOrigin(url) {
      // test that a given url is a same-origin URL
      // url could be relative or scheme relative or absolute
      var host = document.location.host; // host + port
      var protocol = document.location.protocol;
      var sr_origin = '//' + host;
      var origin = protocol + sr_origin;
      // Allow absolute or scheme relative URLs to same origin
      return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
          (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
          // or any other URL that isn't scheme relative or absolute i.e relative.
          !(/^(\/\/|http:|https:).*/.test(url));
  }

  $.ajaxSetup({
      beforeSend: function(xhr, settings) {
          if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
              // Send the token to same-origin, relative URLs only.
              // Send the token only if the method warrants CSRF protection
              // Using the CSRFToken value acquired earlier
              xhr.setRequestHeader("X-CSRFToken", csrftoken);
          }
      }
  });

});