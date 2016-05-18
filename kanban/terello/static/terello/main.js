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
  var $lists = $('.list ul');

  // render a task (put it in the screen)
  var renderEntry = function(entry) {
    var template = '<li><span class="title"></span>' +
                    ' <a href="javascript:;" data-action="delete"><i class="fa fa-trash-o" aria-hidden="true"></i></a> ' +
                    '<a href="javascript:;" data-action="edit"><i class="fa fa-pencil-square-o" aria-hidden="true"></i></a>' +
                    '<form style="display:none;">' +
                    '<span>Title </span>'+
                    '<input type="text" name="title" value="'+entry.title+'" /><br />' +
                    '<span>Status </span>'+
                    '<select name="status">' +
                      '<option value="Today">Today</option>' +
                      '<option value="Week">Week</option>' +
                      '<option value="Month">Month</option>' +
                      '<option value="Year">Year</option>' +
                      '<option value="Done">Done!</option></select><br />' +

                   '<span>Priority </span>'+
                   '<select name="priority">' +
                      '<option value="Urgent">Urgent</option>' +
                      '<option value="High">High</option>' +
                      '<option value="Medium">Medium</option>' +
                      '<option selected="selected" value="Low">Low</option></select><br />' +

                   '<input type="submit" value="Update Task"></form><br /></li>';

    console.log(entry);
    var $row = $(template);
    var $li = $('<li>');
    $row.data('id', entry.id);
    if (entry.status == 'Today') {
      $row.appendTo($('#Today'));
    } else if(entry.status == 'Week') {
      $row.appendTo($('#Week'));
    } else if(entry.status == 'Month') {
      $row.appendTo($('#Month'));
    } else if(entry.status == 'Year') {
      $row.appendTo($('#Year'));
    } else if(entry.status == 'Done') {
      $row.appendTo($('#Done'));
    }
    $row.find('span.title').text(entry.title);

  }

  // get existing tasks
  $.get('api/tasks', function(entries){
    entries.results.forEach(renderEntry);
  });

  // delete a task and remove entry from UI
  $lists.on('click', 'a[data-action="delete"]', function(event) {
    var $row = $(event.target).closest('li');
    var id = $row.data('id');
    $.ajax({
      method: 'delete',
      url:'api/tasks/' + id,
      success: function(){
        $row.remove();
      }
    })
  });

  // edit a task
  $lists.on('click', 'a[data-action="edit"]', function(event) {
    var $row = $(event.target).closest('li');
    $row.find('form').toggle();
  });

  // submit edited task
  $lists.on('submit', 'form', function(event) {
    var $row = $(event.target).closest('li');
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
      url:'api/tasks/' + id + '/',
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
      url: 'api/tasks/',
      data: data,
      success: renderEntry
    });
    return false;
  });
});
