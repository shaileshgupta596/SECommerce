var listElm = document.querySelector("#infinite-scroll")
console.log(listElm.scrollTop, listElm.clientHeight, listElm.scrollHeight)

listElm.addEventListener('scroll', function(){
    if(listElm.scrollTop + listElm.clientHeight == listElm.scrollHeight){
        console.log("Hello");
    }

    console.log("Hello");
})