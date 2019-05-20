var createError = require('http-errors');
var express = require('express');
var path = require('path');
var bodyParser=require('body-parser')
var cookieParser = require('cookie-parser');
var logger = require('morgan');
var mongo=require('mongodb');
var mongoose=require('mongoose');
mongoose.connect('mongodb://localhost/loginapp');
var db=mongoose.connection;

var routes = require('./routes/index');
var users = require('./routes/users');

var app = express();

// view engine setup
//app.set('views', path.join(__dirname, 'views'));
//app.set('view engine', 'hjs');

//assign the swig view engine to .html files....
var swig=require('swig');
app.engine('html',swig.renderFile);
//view angine setup
app.set('views',path.join(__dirname,'views'));
app.set('view engine','html');

app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));

app.use('/', routes);

app.use('/users', users);



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
