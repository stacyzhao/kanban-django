// using csrf token
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

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
  beforeSend: function(xhr, settings) {
    if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
      xhr.setRequestHeader("X-CSRFToken", csrftoken);
    }
  }
});


jQuery(function($) {
  var $entries = $('#entries');

  // render a task (put it in the screen)
  var renderEntry = function(entry) {
    var template = '<li><span class="title"></span>' +
                   ' <a href="javascript:;" data-action="delete"><i class="fa fa-trash-o" aria-hidden="true"></i></a> ' +
                   '<a href="javascript:;" data-action="edit"><i class="fa fa-pencil-square-o" aria-hidden="true"></i></a>' +
                   '<form style="display:none;">' +
                   '<input type="text" name="title" value="'+entry.title+'" />' +
                   '<span>Status</span>'+
                   '<select name="status">' +
                     '<option value="1">Today</option>' +
                     '<option selected="selected" value="2">Week</option>' +
                     '<option value="3">Month</option>' +
                     '<option value="4">Year</option>' +
                     '<option value="5">Done!</option></select>' +

                   '<select name="priority">' +
                     '<option value="1">Urgent</option>' +
                     '<option value="2">High</option>' +
                     '<option value="3">Medium</option>' +
                     '<option selected="selected" value="4">Low</option></select>' +

                   '<input type="submit" value="Update Task"></form></li>';
    console.log(entry);
    var $row = $(template);
    $row.data('id', entry.id);
    $row.find('span.title').text(entry.title);
    $row.appendTo($entries);
  }

  // get existing tasks
  $.get('http://localhost:8000/api/tasks', function(entries){
    entries.results.forEach(renderEntry);
  });

  // delete a task and remove entry from UI
  $entries.on('click', 'a[data-action="delete"]', function(event) {
    var $row = $(event.target).closest('li');
    var id = $row.data('id');
    $.ajax({
      method: 'delete',
      url:'http://localhost:8000/api/tasks/' + id,
      success: function(){
        $row.remove();
      }
    })
  });

  // edit a task
  $entries.on('click', 'a[data-action="edit"]', function(event) {
    var $row = $(event.target).closest('li');
    $row.find('form').toggle();

  });
  // submit edited task
  $entries.on('submit', 'form', function(event) {
    var $row = $(event.target).closest('li');
    debugger;
    var id = $row.data('id');
    var $title = $row.find('input[name="title"]');
    var $status = $row.find('select[name="status"]');
    var $priority = $row.find('select[name="priority"]');
    var data = {
      title: $title.val(),
      status: $status.val(),
      priority: $priority.val(),
    };
    $.ajax({
      method: 'put',
      url:'http://localhost:8000/api/tasks/' + id + '/',
      data: data,
      success: function(response){
        $row.find('span.title').text(response.title);
        $row.find('form').toggle()


      }
    });

    return false;
  });

  // create a new task and display entry
  var $title = $('input[name="title"]');
  var $status = $('select[name="status"]');
  var $priority = $('select[name="priority"]');
  var $form = $('#post-form');
  $form.submit(function() {
    var data = {
      title: $title.val(),
      status: $status.val(),
      priority: $priority.val(),
    };

    console.log('you submitted the form');
    $.ajax({
      method: 'post',
      url: 'http://localhost:8000/api/tasks/',
      data: data,
      success: renderEntry

    });


    return false;
  });

});
