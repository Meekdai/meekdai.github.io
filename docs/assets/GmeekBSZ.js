function loadResource(type, attributes, callback) {
    var element;
    if (type === 'script') {
        element = document.createElement('script');
        element.src = attributes.src;
        element.onload = callback;
    } else if (type === 'link') {
        element = document.createElement('link');
        element.rel = attributes.rel;
        element.href = attributes.href;
    } else if (type === 'style') {
        element = document.createElement('style');
        element.rel = 'stylesheet';
        element.appendChild(document.createTextNode(attributes.css));
    }
    document.head.appendChild(element);
}

function createBSZ() {

    var postBody = document.getElementById('postBody');
    var parent = postBody.parentNode;
    var bszElement = document.createElement('div');
    bszElement.id = 'busuanzi';
    bszElement.innerHTML = "本文浏览量 ";
    // bszElement.style.display='none';
    bszElement.style.float="left";
    bszElement.style.margin="8px";

    var sitePV = document.createElement('span');
    sitePV.id = 'busuanzi_value_site_pv';

    bszElement.appendChild(sitePV);
    parent.insertBefore(bszElement, postBody.nextSibling);
}


document.addEventListener("DOMContentLoaded", function() {
    createBSZ();
    loadResource('script', { src: '//busuanzi.ibruce.info/busuanzi/2.3/busuanzi.pure.mini.js' });
});
