
  function turn_off() {
    $('#status-msg').attr('class', 'off');
    $('#status-msg').html("off");
    $('#status-button').attr('class', 'btn btn-success');
    $('#status-button').html('Turn ON');
  }

  function turn_on() {
    $('#status-msg').attr('class', 'on');
    $('#status-msg').html("on");
    $('#status-button').attr('class', 'btn btn-danger');
    $('#status-button').html('Turn OFF');
  }
  
  function checking() {
    $('#status-msg').attr('class', '');
    $('#status-msg').html("checking...");
    $('#status-button').attr('class', 'btn');
    $('#status-button').html('checking...');
  }
  
  function check_lamp_status() {
    $.ajax({url: "get_lamp_status.php", success: function(result){
        if (result == 1) turn_on();
        else if (result == 0) turn_off();
        else checking();
    }});
  }

  function change_lamp_status() {
    $.ajax({url: "change_lamp_status.php"});
  }