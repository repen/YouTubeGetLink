var url = "https://r1---sn-n8v7kn7z.googlevideo.com/videoplayback?expire=1573656147&ei=88HLXam8Fc7AgQerkoW4Aw&ip=195.176.3.23&id=o-ALqIwPbL2Evj0Vb72xGs_Ka6QNUL5Xba5Y2mxCldZ2iu&itag=18&source=youtube&requiressl=yes&mime=video%2Fmp4&gir=yes&clen=323974167&ratebypass=yes&dur=5291.223&lmt=1540635944814762&fvip=1&fexp=23842630&c=WEB&txp=5531432&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cmime%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=ALgxI2wwRQIgSPa3Og6C-3A9QdEwrs78Kh0i84R7-IqWPcAuC96yKvMCIQCrlufHeMyda0G7z2d0MhWpEwkjhCzxu2qi1y9GRv4ktw%3D%3D&rm=sn-nfpuji-1gil7e,sn-1gies7e&req_id=d84547f5b56a3ee&redirect_counter=2&cms_redirect=yes&ipbypass=yes&mip=92.43.85.72&mm=29&mn=sn-n8v7kn7z&ms=rdu&mt=1573643200&mv=m&mvi=0&pl=24&lsparams=ipbypass,mip,mm,mn,ms,mv,mvi,pl&lsig=AHylml4wRAIgGNAl3MNcZOGqDEh7UBQ5wtb5pxwlD45jvPAwlvHHVY0CIGxLAjvV7U0Pf0_D11x5ebfpZJ2EdeHu97Dg9z6M-bYC";
var xhttp = new XMLHttpRequest();
xhttp.open('HEAD', url);
xhttp.onreadystatechange = function () {
    if (this.readyState == this.DONE) {
        console.log(this.status);
        console.log(this.getResponseHeader("Content-Type"));
    }
};
xhttp.send();