// HTML Casting Variables
const htmlRightAnalog = document.getElementById('rightDriveCtrl');
const htmlLeftAnalog = document.getElementById('leftDriveCtrl');
const htmlPitch = document.getElementById('pitchDriveCtrl');
const htmlYaw = document.getElementById('yawDriveCtrl');
const htmlHeight = document.getElementById('heightDriveCtrl');
const htmlLights = document.getElementById('lightsCtrl');

// Create Gamepad Constants
window.gamepads = null;
window.standardGamepad = null;
window.controllerCode = null;

// Define current payload variables
var currentPitch = 0;
var currentYaw = 0;
var currentHeight = 0;
var currentDriveR = 0;
var currentDriveL = 0;
var currentLightsStatus = false;

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

// export {gamepads};

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
    socket.send("Controller Connected");
}

function disconnectHandler(e) {
    console.log("Gamepad Disconnected")
    document.getElementById("ctrlStatus").classList =  "btn btn-danger";
    document.getElementById("robotStatus").innerHTML = "Gamepad Disconnected"
    removeGamepad(gamepads);
}

function removeGamepad(gamepads) {
    console.log("Gamepad is now disconnected and removed from cache")
  gamepads = null;
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


// Socket.io Variables
// import { gamepads } from "./ctrl.js";
const socket = io('http://127.0.0.1:5000'); // Init and connect socketio client

socket.on('connect',function(){
    // A sort of hand shake to tell the server to send Data 
    // socket.send('ctrl');
    document.getElementById("robotStatus").innerHTML =  "WSIO Status: Connected";
})

socket.on('message',function(msg){
    // Receiving data and asking for data back, will also serve as the controller feedback and accumulation  
    // console.log("Step 2 receive Array data via WS")
    if (msg.length != 0 ){
        document.getElementById("displayVoltage").innerHTML = msg[0];
        document.getElementById("displayTemp").innerHTML = msg[1];
        document.getElementById("displayHumidity").innerHTML = msg[2];
        document.getElementById("xTilt").innerHTML = msg[3];
        document.getElementById("yTilt").innerHTML = msg[4];
        document.getElementById("zTilt").innerHTML = msg[5];
        document.getElementById("xAccel").innerHTML = msg[6];
        document.getElementById("yAccel").innerHTML = msg[7];
        document.getElementById("zAccel").innerHTML = msg[8];
        document.getElementById("xMag").innerHTML = msg[9];
        document.getElementById("yMag").innerHTML = msg[10];
        document.getElementById("zMag").innerHTML = msg[11];
        document.getElementById("gps").innerHTML = msg[12];
        document.getElementById("range").innerHTML = msg[13];

        // console.log("Step 3: Finished changing HTML Data")
    } else {
        alert("Unexpected Signal... System my need to be reset. \nProceed With Caution.");
    }
    

    if (gamepads[0].connected){
      // Drive
      currentDriveL = getAnalog((((gamepads[0].axes[1])*-50)+50).toFixed(0)); // Left
      currentDriveR = getAnalog((((gamepads[0].axes[3])*-50)+50).toFixed(0)); // Right

      // Payload Trim
       if (gamepads[0].buttons[12].pressed){ // pitch up
          if (currentPitch > 254){
            currentPitch = 254;
          } else {
            currentPitch = currentPitch + .1;
          }}

       if (gamepads[0].buttons[13].pressed){ // pitch down
        if (currentPitch < 1){
          currentPitch = 1;
        } else{
          currentPitch = currentPitch - .1;
        }}

       if (gamepads[0].buttons[14].pressed){ // yaw left
        if (currentYaw > 254){
          currentYaw = 254;
        } else {  
          currentYaw = currentYaw + .1;
        }}

       if (gamepads[0].buttons[15].pressed){ // yaw right
        if (currentYaw < 1){
          currentYaw = 1;
        } else {
          currentYaw = currentYaw - .1;
        }}
      
      // Payload Height
      if (gamepads[0].buttons[4].pressed){ // increment height down
        if (currentHeight > 254){
          currentHeight = 254;
        } else {
          currentHeight = currentHeight + .1;
        }}

      if (gamepads[0].buttons[5].pressed){ // increment height up
        if (currentHeight < 1){
          currentHeight = 1;
        } else {
          currentHeight = currentHeight - .1;
        }}

      if (gamepads[0].buttons[8].pressed){ // Retract Arm
        currentHeight = 0;
        currentPitch = 0;
        currentYaw = 0;
        }
      if (gamepads[0].buttons[9].pressed){ // Deploy Arm
        currentHeight = 100;
        currentPitch = 100;
        currentYaw = 100;
        }

      // Lights
      if (gamepads[0].buttons[2].pressed){ // Lights Ons
        currentLightsStatus = true;
        }
      if (gamepads[0].buttons[0].pressed){ // Lights Off
        currentLightsStatus = false;
        }

      htmlLeftAnalog.textContent = Math.round(currentDriveL);
      htmlRightAnalog.textContent = Math.round(currentDriveR);
      htmlPitch.textContent = Math.round(currentPitch);
      htmlYaw.textContent = Math.round(currentYaw);
      htmlHeight.textContent = Math.round(currentHeight);
      htmlLights.textContent = currentLightsStatus;
    // controllerCode to send to python
    controllerCode = [
      Math.round(currentDriveL), 
      Math.round(currentDriveR), 
      Math.round(currentPitch), 
      Math.round(currentYaw), 
      Math.round(currentHeight),
      currentLightsStatus
    ]; 
    // console.log(controllerCode);
    socket.send(controllerCode); // Send out to Receive more
    // console.log("Socket sent data to server")
  
    }

})

socket.on('disconnect',function(){
    document.getElementById("robotStatus").innerHTML =  "WSIO Status: Disconnected";
})


