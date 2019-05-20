var createError = require('http-errors');
var express = require('express');
var path = require('path');
var cookieParser = require('cookie-parser');
var logger = require('morgan');
const { spawn } = require('child_process');
var bodyParser = require('body-parser');
var fs=require('fs');
var output_array;
var output_array2;

var indexRouter = require('./routes/index');
var usersRouter = require('./routes/users');
var usermodule=require('./routes/usermodule');
var adminmodule=require('./routes/adminmodule');
var nativetrees=require('./routes/nativetrees');
var wqc=require('./routes/wqc');

var app = express();
var a;
var b;
var c;
var d;

// view engine setup
// app.set('views', path.join(__dirname, 'views'));
// app.set('view engine', 'hjs');

var swig=require('swig');
app.engine('html', swig.renderFile);
app.set('views', path.join(__dirname,'views'));
app.set('view engine', 'html');

app.use(logger('dev'));
app.use(express.json());
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(bodyParser.json());

app.use('/', indexRouter);
app.use('/users', usersRouter);
app.use('/usermodule', usermodule);
app.use('/adminmodule', adminmodule);
app.use('/nativetrees', nativetrees);
app.use('/wqc', wqc);


app.post("/userinput", function(req, res){

  fs.writeFile('userinput.txt',req.body.district+'\n'+req.body.year+'\n'+ req.body.month, function(err){
    if(err){
     console.log(err);
   
    }
    console.log("file created");
   
   
    });
   
     
     const child = spawn('python', ['rain.py' ]);
     //  console.log(req.body.year);
     //  console.log(req.body.month);
     //  process.stdin.pipe(child.stdin);
   
     file=fs.createReadStream('userinput.txt');
   file.pipe(child.stdin);
   
     
     child.stdout.on('data', (data) => {
       b=data;
      //  console.log(`Population Prediction:\n${data}`);
       console.log(b.toString('utf8'));
     });
    
     setTimeout(myFunction, 7000)
     function myFunction() {
       b=b+'';
        output_array=b.split('\n');
   
       // res.send(b.toString('utf8'));
       // res.send( output_array);
   
       res.render('useroutput', {
        curr1: output_array[0],
        curr2:output_array[1],
        curr3:output_array[2],
        curr4: output_array[3],
        curr5:output_array[4],
        curr6:output_array[5],

   
       }
         
         ); 
      
     //    for(int i=0;i<)
      }
   
   
    }


);

app.post("/userinput2", function(req, res){

  fs.writeFile('userinput2.txt',req.body.year, function(err){
    if(err){
     console.log(err);
   
    }
    console.log("file created");
   
   
    });
   
     
     const child = spawn('python', ['wqc.py' ]);
     //  console.log(req.body.year);
     //  console.log(req.body.month);
     //  process.stdin.pipe(child.stdin);
   
     file=fs.createReadStream('userinput2.txt');
   file.pipe(child.stdin);
   
     
     child.stdout.on('data', (data) => {
       d=data;
      //  console.log(`Population Prediction:\n${data}`);
       console.log(d.toString('utf8'));
     });
    
     setTimeout(myFunction, 7000)
     function myFunction() {
       d=d+'';
        output_array3=d.split('\n');
   
       // res.send(b.toString('utf8'));
       // res.send( output_array);
   
       res.render('wqcoutput', {
        iron: output_array3[0],
        floride:output_array3[1],
        salinity:output_array3[2],
        nitrade: output_array3[3],
        arsenic:output_array3[4],
        other:output_array3[5],

   
       }
         
         ); 
      
     //    for(int i=0;i<)
      }
   
   
    }


);

app.post("/admininput", function(req, res){
  //  res.send("Have a look on console");
  
 fs.writeFile('admininput.txt',req.body.district+'\n'+req.body.supply+'\n'+req.body.year+'\n'+ req.body.month, function(err){
 if(err){
  console.log(err);

 }
 console.log("file created");


 });

  
  const child2 = spawn('python', ['adminmodule.py' ]);
  //  console.log(req.body.year);
  //  console.log(req.body.month);
  //  process.stdin.pipe(child.stdin);

  file=fs.createReadStream('admininput.txt');
file.pipe(child2.stdin);

  
  child2.stdout.on('data', (data) => {
    c=data;
   //  console.log(`Population Prediction:\n${data}`);
    console.log(c.toString('utf8'));
  });
 
  setTimeout(myFunction, 8000)
  function myFunction() {
    c=c+'';
     output_array2=c.split('\n');

    // res.send(b.toString('utf8'));
    // res.send( output_array);

    res.render('adminoutput', {
     
      op1:output_array2[0],
      op2:output_array2[1],
      op3:output_array2[2],
      op4:output_array2[3],
      op5:output_array2[4],
      op6:output_array2[5],
      op7:output_array2[6],
      op8:output_array2[7],
      op9:output_array2[8],
      op10:output_array2[9],
      op11:output_array2[10],
      


    }
      
      ); 
   
  //    for(int i=0;i<)
   }


 }
 );

 app.post("/login", function(req, res){
   if(req.body.key=="123abc"){
  res.redirect('/adminmodule');
   }
   else{
        res.send("Unauthorized User");

   }





 });

// catch 404 and forward to error handler
app.use(function(req, res, next) {
  next(createError(404));
});

// error handler
app.use(function(err, req, res, next) {
  // set locals, only providing error in development
  res.locals.message = err.message;
  res.locals.error = req.app.get('env') === 'development' ? err : {};

  // render the error page
  res.status(err.status || 500);
  res.render('error');
});

module.exports = app;
