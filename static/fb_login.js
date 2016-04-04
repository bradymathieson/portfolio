function statusChangeCallback(response) {
  console.log('statusChangeCallback');
  console.log(response);

  if (response.status === 'connected') {
    printName();
    showPhoto();
  } else if (response.status === 'not_authorized') {
    document.getElementById('status').innerHTML = 'world';
  } else {
    document.getElementById('status').innerHTML = 'world';
  }
}

function checkLoginState() {
  FB.getLoginStatus(function(response) {
    statusChangeCallback(response);
  });
}

window.fbAsyncInit = function() {
FB.init({
  appId      : '698534526916884',
  cookie     : true,  
  xfbml      : true,  
  version    : 'v2.5'
});

FB.getLoginStatus(function(response) {
  statusChangeCallback(response);
});

};

(function(d, s, id) {
  var js, fjs = d.getElementsByTagName(s)[0];
  if (d.getElementById(id)) return;
  js = d.createElement(s); js.id = id;
  js.src = "//connect.facebook.net/en_US/sdk.js";
  fjs.parentNode.insertBefore(js, fjs);
}(document, 'script', 'facebook-jssdk'));

function printName() {
  console.log('Welcome!  Fetching your information.... ');
  FB.api('/me', function(response) {
    console.log('Successful login for: ' + response.name);
    var name = response.name;
    var sep = name.split(" ");
    document.getElementById('status').innerHTML =
      sep[0];
  });
}