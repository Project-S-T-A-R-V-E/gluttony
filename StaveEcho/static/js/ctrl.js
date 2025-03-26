// HTML Casting Variables
const htmlRightAnalog = document.getElementById('rightDriveCtrl');
const htmlLeftAnalog = document.getElementById('leftDriveCtrl');
const htmlPitch = document.getElementById('pitchDriveCtrl');
const htmlYaw = document.getElementById('yawDriveCtrl');
const htmlHeight = document.getElementById('heightDriveCtrl');

// Create Gamepad Constants
var gamepads
var standardGamepad

// Define current payload variables
currentPitch = 0;
currentYaw = 0;
currentHeight = 0;
currentDriveR = 0;
currentDriveL = 0;

// Check for initial gamepad connection
var haveEvents = 'GamepadEvent' in window; // is there a case of gamepad usage in the window
var haveWebkitEvents = 'WebKitGamepadEvent' in window;
var controllers = {};
var rAF = window.mozRequestAnimationFrame || window.webkitRequestAnimationFrame || window.requestAnimationFrame;

// Check for web browser support
if (haveEvents) {
  // Chrome and Firefox and Edge
  console.log("Use Chrome Firefox and Edge Framework")
  window.addEventListener("gamepadconnected", connectHandler);
  window.addEventListener("gamepaddisconnected", disconnectHandler);
} else if (haveWebkitEvents) {
  // Safari
  console.log("Safari")
  window.addEventListener("webkitgamepadconnected", connectHandler);
  window.addEventListener("webkitgamepaddisconnected", disconnectHandler);
} else {
  setInterval(scangamepads, 500);
  console.log("Looking for Gamepad");
}



//   Gamepad Functions
function connectHandler(e) {
  addGamepad(e.gamepad);
}

function addGamepad() {
  console.log("New gamepad detected")
  gamepads = navigator.getGamepads();
    standardGamepad = {
        id: gamepads[0].id,
        Laxes: gamepads[0].axes[1].toFixed(2),
        Raxes: gamepads[0].axes[3].toFixed(2),
        ArmUp: gamepads[0].buttons[5].pressed,
        ArmDown: gamepads[0].buttons[4].pressed,
        FireOne: gamepads[0].buttons[3].pressed,
        FireTwo: gamepads[0].buttons[12].pressed,
        ctrlRetractArm: gamepads[0].buttons[9].pressed,
        ctrlDeployArm: gamepads[0].buttons[8].pressed
    } 
    document.getElementById("ctrlStatus").classList =  "btn btn-success";
    document.getElementById("robotStatus").innerHTML = "The " + gamepads[0].id + " has connected successfully";
}

function disconnectHandler(e) {
    console.log("Gamepad Disconnected")
    document.getElementById("ctrlStatus").classList =  "btn btn-danger";
    document.getElementById("robotStatus").innerHTML = "Gamepad Disconnected"
    removeGamepad(gamepads);
}

function removeGamepad(gamepads) {
    console.log("Gamepad is now disconnected and removed from cache")
  delete gamepads;
}

function updateStatus() {
  scanGamepads();
  for (j in controllers) {
    var controller = controllers[j];
    var d = document.getElementById("controller" + j);
    var buttons = d.getElementsByClassName("button");
    for (var i=0; i<controller.buttons.length; i++) {
      var b = buttons[i];
      var val = controller.buttons[i];
      var pressed = val == 1.0;
      var touched = false;
      if (typeof(val) == "object") {
        pressed = val.pressed;
        if ('touched' in val) {
          touched = val.touched;
        }
        val = val.value;
      }
      var pct = Math.round(val * 100) + "%";
      b.style.backgroundSize = pct + " " + pct;
      b.className = "button";
      if (pressed) {
        b.className += " pressed";
      }
      if (touched) {
        b.className += " touched";
      }
    }

    var axes = d.getElementsByClassName("axis");
    for (var i=0; i<controller.axes.length; i++) {
      var a = axes[i];
      a.innerHTML = i + ": " + controller.axes[i].toFixed(4);
      a.setAttribute("value", controller.axes[i]);
    }
  }
  rAF(updateStatus);
}

function scanGamepads() {
  var gamepads = navigator.getGamepads ? navigator.getGamepads() : (navigator.webkitGetGamepads ? navigator.webkitGetGamepads() : []);
  for (var i = 0; i < gamepads.length; i++) {
    if (gamepads[i] && (gamepads[i].index in controllers)) {
      controllers[gamepads[i].index] = gamepads[i];
    }
  }
}

function getAnalog(anaNum) {
    // The -100:100 analog signal from the controller is not inherently compatible with the Arduino Signal that is expected/planned. So this function makes it a two digit signal and limits it from 00:99 
    if (anaNum == 0){
    return "00";
    } else if(anaNum==100){
        return "99"
    } else if (anaNum.length == 1){
        return "0"+ anaNum
    } else {
        return anaNum
    }
}

function formatTripleDigit(digit,type){ 
    if (digit <= "0"){
        return "000";
    } else if (digit > 0 && digit < 10) {
        return "00" + digit.toString();
    } else if (digit >= 10 && digit < 100) {
        return "0" + digit.toString();
    } else if (digit >= 100 ) {
        if (type == "psi" && digit >= 110){
          return "110";
        } else if (type == "arm" && digit >= 255){
          return "255";
        } else {
          return digit;
        }
    } 
} 

function getDigital(dSignal){
    // The gamepad API returns true or false. So this function will return a "1" or "0" for the planned final Signal 
    if (dSignal == true){
        return "1";
    } else {
        return "0"
    }
}


