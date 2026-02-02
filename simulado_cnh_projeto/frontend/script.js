
let questoes = []
let atual = 0
let acertos = 0

async function iniciar(){
 const r = await fetch('http://127.0.0.1:5000/simulado')
 questoes = await r.json()
 document.getElementById('inicio').style.display='none'
 document.getElementById('quiz').style.display='block'
 mostrar()
}

function mostrar(){
 let q = questoes[atual]
 document.getElementById('pergunta').innerText = q.pergunta

 let html=''
 q.alternativas.forEach((a,i)=>{
   html += `<div class="form-check">
     <input class="form-check-input" type="radio" name="alt" value="${a.correta}" id="a${i}">
     <label class="form-check-label" for="a${i}">${a.texto}</label>
   </div>`
 })
 document.getElementById('alternativas').innerHTML = html
}

function proxima(){
 let marcada = document.querySelector('input[name=alt]:checked')
 if(!marcada) return alert('Escolha uma opção')

 if(marcada.value=='true') acertos++

 atual++
 if(atual < questoes.length){
   mostrar()
 }else{
   fim()
 }
}

function fim(){
 document.getElementById('quiz').style.display='none'
 document.getElementById('resultado').style.display='block'
 document.getElementById('resultado').innerHTML =
   `<h3>Resultado: ${acertos} de ${questoes.length}</h3>`
}
