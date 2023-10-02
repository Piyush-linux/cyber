---
title: "Deno (A Starter Pack)"
description: "Lets learn all basic function and create some app together"
publishDate: "12 Sep 2023"
tags: ["deno","backend"]
---



## CLI App 1 (I/O)

### Pseudo Steps
1. Get User Name
2. Ask if they like cat
3. If YES Get kitten name and write person & kitten name into cat.txt
4. If NO then only write person name into cat.txt

### Code
```js
const name = prompt("Whats your name :")
console.log(`Hello ${name}`) 
const catQ = confirm("Are you a cat person : ")
if (catQ) {
    console.log("Good kitty :)")
	const cat = prompt("Your kitten name :")
    let data = `Name: ${name} \nKitten: ${cat}`
    await Deno.writeTextFile("cat.txt", data)
} else {
    console.log("Bad kitty :(")
    let data = `Name: ${name}`
    await Deno.writeTextFile("cat.txt", data)
}
```
### Run
```sh
deno run --allow-write cli.ts
```


## CLI App 2

### Pseudo Steps
1. chk if todos.txt exist
2. if not then create
3. take task : assign id & name
4. JSON -> id:Number , task:String , check:bool
5. List() , Add() , Del() , Help()


### Code
```js


let opr = Deno.args
// @ console.log(opr)

// -- help
let help = () => {
    console.log("\n--- Task Application ---")
    console.log("> keep trask of your todo and get finished with your work :)")
    console.log("")
    console.log("            list : To list all todos")
    console.log(" add <id> <task> : To Add task")
    console.log("        del <id> : To Delete task")
    console.log("")
}

// -- List < tasks
let List = async () => {
    let data = JSON.parse(await Deno.readTextFile("./todos.json"));
    console.log("--- Task\n");
    await data.map((x) => {
        console.log(`[ ] ${x.task}`)
    })
    console.log("");
}

// -- Add < ID , Task >
let Add = async () => {
    let id = Number.parseInt(opr[1])
    let task = opr[2]
    let data = JSON.parse(await Deno.readTextFile("./todos.json"));
    let sample_task = { id: id, task: task, check: false }
    let newData = [...data, sample_task]
    console.log(newData)
    await Deno.writeTextFile('./todos.json', JSON.stringify(newData));
}

// -- Del
let Del = async () => {
    let data = JSON.parse(await Deno.readTextFile("./todos.json"));
    let id = prompt("ID Name : ")
    let index;
    let dataa = await data.find((x, i) => {
        if (x.id == id) {
            index = i;
            return i
        } else {
            index = null
        }
    })
    if (index) {
        const removed_todo = data.splice(index, 1);
    }
    await Deno.writeTextFile('./todos.json', JSON.stringify(data));
}


//-- Main Fn
if (opr == "-h" || opr == "--help") {
    help()
} else if (opr[0] == "list") {
    await List()
} else if (opr[0] == "add") {
    await Add()
} else if (opr == "del") {
    await Del()
}
```

### Run
```sh
deno run --allow-write --allow-read cli2.ts -h
deno run --allow-write --allow-read cli2.ts list
deno run --allow-write --allow-read cli2.ts add 2 hello 
deno run --allow-write --allow-read cli2.ts del 2
```


## Web App 1 (News Scrapper)

### [C O D E](https://github.com/me0w-me0w-me0w/dig)


```yml
# data.yml
- link: "https://news.itsfoss.com/tag/first-look/"
  route: "/news/1"
  path: "absolute"
  parent: ".js-grid.o-grid.o-grid--4-columns"
  child: "a"
  value: false
  attr: "src"
- link: "https://linuxhint.com/"
  route: "/news/2"
  path: "relative"
  parent: ".vce-loop-wrap"
  child: "a"
  value: false
  attr: "src"
```

```js
// index.ts
import * as cheerio from "https://esm.sh/cheerio@1.0.0-rc.12";
import { Application, Router } from "https://deno.land/x/oak/mod.ts";
import {
    parse as yamlParse,
    parseAll as yamlParseAll,
    stringify as yamlStringify,
  } from 'https://deno.land/std@0.82.0/encoding/yaml.ts';
const router = new Router();


const data = yamlParse(await Deno.readTextFile('data.yaml'));

router.get("/", (ctx) => {
    ctx.response.body = "Welcome To pscraper";
});

data.map((e)=>{
  router.get(e.route, async(ctx) => {
    let res = await fetch(e.link);
    let html = await res.text()
    const $ = cheerio.load(html);
    let cls = e.parent
    let api = []
    let o = $(cls).html()
      // console.log('req : ' + $(cls).html() )
    let dom = $(cls).children().each(function (index) {
      //-----  console.log(index)
        let url = $(this).find('a').attr('href')
        // console.log(url)
        if(e.path == 'absolute'){
          api.push({ 
          		site: e.link , 
          		url: `https://news.itsfoss.com${url}` 
          	})
        }else{
          api.push({ 
          	site:e.link , 
          	url: url 
          })
        }
    })
    // ctx.response.body = api;
    ctx.response.body = api;
  });
})

const app = new Application();
app.use(router.routes());
app.use(router.allowedMethods());

app.addEventListener('listen', () => {
    console.log("--------------- Listening on http://localhost:8080")
})

await app.listen({ port: 8080 });
```

## Deno API CRUD 1


```js
// http POST :8000/cats  \
// id:=3 \
// name=joeeee

import { Application, Router  } from "https://deno.land/x/oak/mod.ts";
const router = new Router();
const PORT = 8000
const HOST ='127.0.0.1'


let cats = [{
  id:1,
  name:"lisa",
},{
  id:2,
  name:"rani",
},{
  id:3,
  name:"meow",
},]

let get_cats = ({response})=>{
  response.status = '200'
  response.body = cats
}

let get_cat = ({params , response})=>{
  let cat = cats.find( (x)=> x.id == params.id )
  response.body = cat
}
// post require  : async_await
let add_cat = async ({ request , response })=>{
  let newCat = await request.body().value
  // let cat = cats.find( (x)=> x.id == params.id )
  cats.push(newCat)
  response.body = cats;
}

let remove_cat =({params, response})=>{
  let delCat = params.id
      console.log("Del Cat "+delCat)
  let ind = 0;
  cats.map((itm,index)=>{
    // return itm.id == delCat
    if( itm.id == delCat){
      ind = index
    }
  })
  cats.splice(ind,1)
  response.body = cats;
}

router.get("/", ({response})=> response.body("Hello Kittens"))
router.get("/cats", get_cats)
router.get("/cats/:id", get_cat)
router.post("/cats", add_cat)
router.delete("/cats/:id", remove_cat)

const app = new Application();
app.use(router.routes());
app.use(router.allowedMethods());
await app.listen({ hostname: HOST, port: PORT });
```

### 