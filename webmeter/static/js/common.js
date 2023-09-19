
const getLocationParams = () => {
    let href = window.location.href;
    let query = href.substring(href.indexOf("?") + 1);
    let vars = query.split("&");
    let obj = {};
    for (let i = 0; i < vars.length; i++) {
      let pair = vars[i].split("=");
      obj[pair[0]] = pair[1];
    }
    return obj;
  };


const elMessage = (type, message) => {
    switch(type){
        case 'success':
            ElementPlus.ElMessage({
                showClose: true,
                message: message,
                type: 'success',
            })
            break;
        case 'warning':
            ElementPlus.ElMessage({
                showClose: true,
                message: message,
                type: 'warning',
            })
            break;
        case 'error':
            ElementPlus.ElMessage({
                showClose: true,
                message: message,
                type: 'error',
            })
            break;
        default:
            ElementPlus.ElMessage({
                showClose: true,
                message: message,
            })         
    };
}
