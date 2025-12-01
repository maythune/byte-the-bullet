let userResponse = "";
let botResponse = "";
let inputBox;

function setup() {
  createCanvas(1500, 1000);

  inputBox = createInput();
  inputBox.position(100, 800);
  inputBox.size(700);

  // ENTER triggers chatbot
  inputBox.changed(() => {
    userResponse = inputBox.value();
    botResponse = getBotReply(userResponse);
    inputBox.value("");
  });
}

function draw() {
  background(0);

  fill(255);
  textSize(30);
  text("Chatbot Demo", 400, 40);

  textSize(16);
  text("You: " + userResponse, 100, 100, 1000);
  text("Bot: " + botResponse, 100, 140, 1000);
}

function getBotReply(msg) {
  msg = msg.toLowerCase();

  if (msg.includes("hello") || msg.includes("hi")) {
    return "Hello! How can I help you today?";
  }

  if (msg.includes("help")) {
    return "Sure! Tell me what you need help with.";
  }

  if (msg.includes("time")) {
    return "The time now is " + new Date().toLocaleTimeString();
  }

  if (msg.includes("bye")) {
    return "Goodbye!";
  }

  return "I didn't understand that. Try saying 'hello' or 'help'.";
}

