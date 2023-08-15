const { createApp, ref, onMounted } = Vue

const app = createApp({
    setup() {
        const checkedType = ref(true)
        const inputPlan = ref('')
        var plans = ref([])
        
        onMounted(() => {
            console.log('debug')
            plans = initPlan();
            console.log(plans)
        });

        function createPlan(){
            axios.post('/api/plan/create', {
                plan_name: inputPlan.value
            })
            .then(function (response) {
                if(response['data']['status'] == 1){
                    elMessage('success', response['data']['msg'])
                }else{
                    elMessage('error', response['data']['msg'])
                }
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
                elMessage('error', error)
            });
        };

        function initPlan(){
            var plan_list = []
            axios.post('/api/plan/all', {})
            .then(function (response) {
                if(response['data']['status'] == 1){
                    plan_list =  response['data']['plan_list']
                }else{
                    elMessage('error', response['data']['msg'])
                }
                console.log(response);
            })
            .catch(function (error) {
                console.log(error);
                elMessage('error', error)
            });
            console.log(plan_list);
            return plan_list
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

        return {
            checkedType,
            inputPlan,
            createPlan,
            elMessage,
            plans
        };
    }
});
for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
    app.component(key, component)
};
app.use(ElementPlus);
app.mount('#app');