// console.log("Hello world")
// console.log(global.luckyNum)
// globalThis.luckyNum = 23

// console.log(global.luckyNum)
// console.log("user is",process.env.user)
// console.log(process.platform)

// process.on('exit',()=>{
//     console.log("Byee")
// })

// const {EventEmitter} = require('events');
// const eventEmitter = new EventEmitter()

// eventEmitter.on('lunch',()=>{
//     console.log("lets eat sushi")
// })

// eventEmitter.emit("lunch")

// const {readFile, readFileSync}=require('fs')

// const txt= readFileSync('./hello.txt','utf-8')
// console.log(txt)

// const http = require('node:http')

// const hostname = '127.0.0.1'
// const port = 3000
// const server = http.createServer(
//     (req,res)=>{
//         res.statuscode = 200;
//         res.setHeader('Content-Type', 'text/plain')
//         res.end("hello world \n")
//     }
// )

// server.listen(port, hostname, ()=>{
//     console.log(`server runniing at http://${hostname}:${port}/`)
// })

// console.log(process.env.NODE_ENV)

// const car1 = require('./my-module')
// const {car} =require('./my-module')

// console.log(car1)
// console.log(car)

// const greet =(name)=>{
//     console.log("hello,",name)
// }
// greet("Mario")
// greet("Yoshi")
// console.log(global)

// global.setTimeout(() => {
//     console.log("Bruhhh")
// }, 3000);
// i=0
// setInterval(
//     ()=>{
//         i+=1
//         console.log("In the interval",i)
//     }, 100
// )
// const os = require('os')

// console.log("file name is === > ",__filename,"\ndir name is === > ",__dirname)

// console.log(os.platform(), os.homedir())

// file system

// const fs = require('fs')
// fs.readFile('./learningnode/hello.txt',(err,data)=>{

//     if(err){
//         console.log(err)
//     }
//     console.log(data.toString())

// })
// console.log("file system is slow")

// const fs = require("fs");

// for (i = 0; i < 9; i++) {
//   console.log("Hello", i);
//   fs.unlink(
//     `./learningnode/hell${i}.txt`,
//     // `Hello Bruh ${i}, Now you dont have control`,
//     (err) => {
//       console.log("Callback function fired, error is", err ? err : "==");
//     }
//   );
// }

// if (!fs.existsSync("./assests")) {
//   fs.mkdir("./assests", (err) => {
//     err ? console.log(err) : {};
//     console.log("directory created");
//   });
// }

// const fs = require("fs");

// const readstream = fs.createReadStream("./learningnode/stream.txt");

// readstream.on("data", (chunk) => {
//   console.log("\n\n - - - - NEW CHUNK - - - - \n\n");
//   console.log(chunk.toString());
// });
const http = require("http");
const fs = require("fs");

const server = http.createServer((req, res) => {
  console.log("REQUEST IS THIS", req.url, req.method);
  res.setHeader("Content-Type", "text/html");

  let path = "./";

  switch (req.url) {
    case "/":
      path += "index.html";
      break;
    case "/index.html":
      path += "index.html";
      break;
    case "/about.html":
      path += "about.html";
      break;
    case "/about-me.html":
      res.statusCode = 301;
      res.setHeader("Location", "/about.html");
      res.end();
      break;
    default:
      path += "404.html";
      break;
  }

  fs.readFile(path, (err, data) => {
    if (err) {
      console.log(err);
      res.end();
    } else {
      res.write(data);
      res.end();
    }
  });

  console.log("RESPONSE IS THIS");
});

server.listen(3000, "localhost", () => {
  console.log("Server listening");
});
