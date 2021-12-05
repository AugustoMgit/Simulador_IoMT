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
            //return axios.post('http://127.0.0.1:5000/api/change/mydado/', dadosColetados);
            return axios.post('/api/change/mydado/', dadosColetados)
            .then(response => dadosColetados = response)
            .catch( error => {            
                console.log(error);
            })
        },

        simulador(dadosSimulados) {
            return axios.post('/api/generatedata', dadosSimulados)
            .then(response => dadosSimulados = response)
            .catch( error => {            
                console.log(error);
            })
        }
    }

}

export default restService;
