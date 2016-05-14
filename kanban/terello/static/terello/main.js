var $entries = $('#entries');

$.get('http://127.0.0.1:8000/api/tasks', function(entries){
  debugger;
  entries.results.forEach(function(entry) {
    console.log(entry)
    var $li = $('<li>');
    $li.text(entry.title)
    $li.appendTo($entries);
  })
})
