import axios from '@/plugins/axios';

// const restApi = axios.create({
//     baseUrl: "http://"
// });


/*
const users = [
    {
        name: 'joao',
        birthday: '2007-11-09',
        gender: 'M'
    },
    { 
        name: 'maria',
        birthday: '2002-11-09',
        gender: 'F'
    },
    {
        name: 'roberson',
        birthday: '1992-11-09',
        gender: 'M'
    }
]
*/

var restService = {

    restApi: {

        dados(dadosColetados) {
            return axios.post('http://127.0.0.1:5000/api/add', dadosColetados);            
        },

        simulador(dadosSimulados) {
            return axios.post('http://127.0.0.1:5000/api/generatedata', dadosSimulados)            
        }
    }

}

export default restService;
