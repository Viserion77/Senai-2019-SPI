const express = require('express');
const app = express();
 
app.use(express.json());

app.get('/activitys', function (req, res) {
  res.send(usualResponse(req,res));
})

app.post('/activitys', function (req, res) {
  res.send(usualResponse(req,res));
})

app.delete('/activitys', function (req, res) {
  res.send(usualResponse(req,res));
})
 
app.listen(3000);

function usualResponse(req,res){
  let response = [];
  res.setHeader('Content-Type','application/json');
  
  console.log('params',req.params);
  response.push({params:req.params});
  
  console.log('query',req.query);
  response.push({query:req.query});
  
  console.log('headers',req.headers);
  response.push({headers:req.headers});
 
  console.log('body',req.body);
  response.push({body:req.body});
 
  console.log('route',req.route);
  response.push({route:req.route});
  return response;
}