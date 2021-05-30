function logindog() {
  const name = document.getElementById('dname').value;
  const passwd = document.getElementById('dpasswd').value;
  fetch("/api/login/", {
    method: 'POST',
    body: JSON.stringify({ 'c': name, 'p': passwd }),
    headers: new Headers({
      'Content-Type': 'application/json'
    })
  }).then(res => res.json())
    .catch(error => console.error('Error:', error))
    .then(data => {
      if (data.r == 's') {
        localStorage.setItem('i', data.i);
        let logina = document.getElementById('appid');
        // logina.style.display = 'none';
        initdog();
      }
      else {
        let aksk = document.getElementById('resddog');
        aksk.innerHTML = `<div class="alert alert-danger alert-dismissible">
                          <button type="button" class="close" data-dismiss="alert">&times;</button>
                          <strong>错误!</strong> 用户名或密码输入错误。
                        </div>`;
      }
    });
}

function initdog() {
  doginfostr = localStorage.getItem('i');
  if (doginfostr === null) {
    console.log('未登录');
    return 'bad';
  }
  // doginfo = JSON.parse(doginfostr);
  ck = $.post("/api/user/",
    {
      i: doginfostr
    },
    function (data, status) {
      // alert("数据: \n" + data + "\n状态: " + status);
      console.log(data)
      if (data.r == 's') {
        let logina = document.getElementById('appid');
        logina.classList.remove("logdog");

        logina.innerHTML = `
        <div class="card" id="iidog2">
        <div id="iidog"><div class="card-body" id="ddinfo"><img src="/static/noface.jpg" class="dogavatar"><span class="dogname">${data.data.username}</span><div class="contain cont"></div></div></div>
        <div class="container">
        
            <p>永久链接:</p>
            <div id="loadm"><input required="required" type="url" placeholder="永久链接" style="width: 100%;" id = "ccc">

            <!-- <form class="form-inline">
                    <label class="form-check-label">
                        <input type="checkbox" id='llio' class="form-check-input" value="">生成图片
                    </label>
                    <div class="form-check">
                        <label for="ptime">过期时间(小时):</label>
                        <input type="number" class="form-control" id="ptime" placeholder="0" value = "0">
                        <label for="rant">显示概率(只对图片有效):</label>
                        <input type="number" class="form-control" id="rant" placeholder="1" value = "1">
                        
                    </div>
                </form>-->
                <br> <br>
                <p>永久链接是指像https://mp.weixin.qq.com/s/PveUS2I4i3EKPIbilXURvg这样的链接。</p>
                <button type="button" class="btn btn-primary" onclick="uploaddog()">发布</button>
                <div>
                    <div id="innf"></div> <span id="smk"></span>
                    <ul id="lldog" class="list-group"></ul>
                </div> <br>
                <div class="container">
                    <div id="dkil" class="tipianl"></div>
                </div>
            </div>
        </div>
        `
      } else {
        localStorage.clear();
        return 'bad';
      }
    });
  // $.post('/api/list/', { i:})
  
  doglist();
}

function uploaddog() {
  const cdog = document.getElementById('ccc').value;
  // const ptime = document.getElementById('ptime').value
  // const rant = document.getElementById('rant').value;
  // const pogc = document.getElementById('llio').checked ? 1 : 0;
  const doginfostr = localStorage.getItem('i');
  if (/https:\/\/mp.weixin.qq.com\/s\//.test(cdog)){
  // console.log({ i: doginfostr, c: cdog, t: ptime, r: rant, g: pogc })
  $.post("/api/create/", { i: doginfostr, c: cdog.replace("https://mp.weixin.qq.com/s/","") }, function (data, status) {
    if (data.r=='ok') {
      var Htmldog4 = `<div class="alert alert-success alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>任务已提交！</strong> ID: ${data.id}</div>`;
      $('#innf').html(Htmldog4);
      document.getElementById('ccc').value='';
    } else
    {
      var Htmldog3 = `<div class="alert alert-danger alert-dismissible"><button type="button" class="close" data-dismiss="alert">&times;</button><strong>错误！</strong> ${data.r}</div>`;
      $('#innf').html(Htmldog3);
    }
  })
  } else {
    alert("格式错误")
  }
}

function doglist(page = 0) {
  var idog = localStorage.getItem('i');
  var ddlist = document.getElementById('ddlist');
  var btdog = document.getElementById('bttdog');
  btdog.style.display="block";
  console.log(ddlist)
  $.post('/api/list/', { i: idog, y: page }, function (data, status) {
    // console.log(data)
    Num = data.n;
    Page = data.p;
    var doghtml='';
    for (let idog = 0; idog < data.data.length; idog++) {
      const element = data.data[idog];
      const dutime = new Date(Number(element.pubtime))
      const sctime =  new Date(element.stime)
      LIST[element.id]=element;
      dht = `<div class="card">
      <div class="card-body" id="${Page}-${idog + 1}">

          <div class="contain cont" id='${element.id}'>
          <h5><a href="${element.url}">${element.title}</a></h5>
          <p>${element.desp}</p>
          <p><button type="button" class="btn btn-danger btn-sm btdogs" onclick="rmddog(this)">删除</button><button type="button" class="btn btn-primary btn-sm btdogs" onclick="cpdog(this)">复制内容</button><button type="button" class="btn btn-primary btn-sm btdogs" onclick="cpdog2(this)">复制内容(fjq测试用)</button><button type="button" class="btn btn-primary btn-sm btdogs" onclick="cpdog3(this)">复制内容(新华号图片测试用)</button></p>
              
          </div>
      </div>
      <div class="card-footer">
          <span class="uadog"> 
          发布时间：${dutime.toLocaleString()} 上传时间: ${sctime.toLocaleString()}</span>
      </div>
  </div>`;
      doghtml +=dht;
    }
    ddlist.innerHTML=doghtml;
    var dogq = document.getElementById('syy');
    var dogh = document.getElementById('xyy');
    if (Page==0) {
      // let dog = document.getElementById('qyy');
      dogq.disabled=true;
    }
    else {
      dogq.disabled=false;
    }
    if (Page==Math.floor(Num/10)) {
      // let dog = document.getElementById('qyy');
      dogh.disabled=true;
    }
    else {
      dogh.disabled=false;
    }
  })
}

function rmddog(afttdog) {
  console.log(afttdog.parentElement.parentElement);
  Rmdog = afttdog.parentElement.parentElement;
  console.log(Rmdog.id);
  var msg = `您真的确定要删除 ID: ${Rmdog.id} 吗？\n\n请确认！`; 
 if (confirm(msg)==true){ 
  idog = localStorage.getItem('i');
  Rmdog.parentElement.parentElement.style.display='none';
  $.post('/api/remove/', { i: idog, c:Rmdog.id },function (data,status) {
    if (data.r=='s') {
      console.log('已删除');
      alert('已删除');
    }
  })
 }else{ 
  return false; 
 } 

}

function nextpage() {
  doglist(Page+1);
}
function lastpage() {
  doglist(Page-1);
}

function copydog(content) {
  var ctr = document.body.createControlRange();

  area.contentEditable = true;

  ctr.addElement(area);

  ctr.execCommand('Copy');

  // area.contentEditable = false;
  // var aux = document.createElement("input"); 
  //   aux.setAttribute("value", content); 
  //   document.body.appendChild(aux); 
  //   aux.select();
  //   document.execCommand("copy"); 
    document.body.removeChild(aux);
    alert("复制成功");
    // if (message == null) {
    //     alert("复制成功");
    // } else{
    //     alert(message);
    // }
}

function cpdog(afttdog) {
  Cpdog = afttdog.parentElement.parentElement;
  console.log(Cpdog.id);
  DogZore.innerHTML=LIST[Cpdog.id].ptext;
  sldog = document.getElementById("dogcp");
  sldog.innerHTML=LIST[Cpdog.id].ptext;
  selectElementContents(sldog);
  sldog.innerHTML='';
  // copydog(`<html>${LIST[Cpdog.id].ptext}</html>`);
}

function cpdog2(afttdog) {
  Cpdog = afttdog.parentElement.parentElement;
  console.log(Cpdog.id);
  DogZore.innerHTML=LIST[Cpdog.id].ptext.replace("</strong>","</b>").replace("<strong>","<b>");
  sldog = document.getElementById("dogcp");
  sldog.innerHTML='<p>'+LIST[Cpdog.id].ptext.replace(/<\/span>/g,"").replace(/<span>/g,"").replace(/<\/strong>/g,"").replace(/<strong>/g,"").replace(/<\/p>/g,"<br>").replace(/<p>/g,"<br>").replace(/(<br>)+/g,"<br>")+'</p>';
  selectElementContents(sldog);
  console.log(sldog.innerHTML);
  //sldog.innerHTML='';
  // copydog(`<html>${LIST[Cpdog.id].ptext}</html>`);
}

function cpdog3(afttdog) {
  Cpdog = afttdog.parentElement.parentElement;
  console.log(Cpdog.id);
  DogZore.innerHTML=LIST[Cpdog.id].ptext.replace("</strong>","</b>").replace("<strong>","<b>");
  sldog = document.getElementById("dogcp");
  sldog.innerHTML=LIST[Cpdog.id].ptext.replace(/https:\/\/mmbiz.qpic.cn/g,"https://wxproxy.dogcraft.top");
  selectElementContents(sldog);
  console.log(sldog.innerHTML);
  //sldog.innerHTML='';
  // copydog(`<html>${LIST[Cpdog.id].ptext}</html>`);
}


function selectElementContents(el) {

  // var body = document.body, range, sel;

  if (document.createRange && window.getSelection) {

      range = document.createRange();

      sel = window.getSelection();

      sel.removeAllRanges();

      // try {
          range.selectNodeContents(el)
          sel.addRange(range);
      // } catch (e) {
      //     range.selectNode(el);
      //     sel.addRange(range);
      // }
      document.execCommand("copy");
      window.getSelection().empty();
      alert("成功复制到剪贴板");
    }

  }
var Num = 0;
var Page = 0;
var LIST = {};
var DogZore = document.createElement("div");



function st() {
  var Locat = localStorage.getItem('location');
  if (Locat === null) {
    Locat = 'admin';  
    localStorage.setItem('location','admin')
  }
  if (Locat==='main') {
    const mainpart = document.getElementById('main')
    const admipart = document.getElementById('admin')
    admipart.style.display = 'none';
    mainpart.style.display = 'block';
    maininit();
  } else {
    const mainpart = document.getElementById('main')
    const admipart = document.getElementById('admin')
    admipart.style.display = 'block';
    mainpart.style.display = 'none';
    admininit();
  }
}

function ctmain() {
  localStorage.setItem('location','main');
  st();
}

function ctadmin() {
  localStorage.setItem('location','admin');
  st();
}

function admininit() {
  initdog();
}
function maininit() {
  
}
st();
// initdog();
