import axios from 'axios';
// import {soap} from 'soap';

// const soapApi = axios.create({
//     baseUrl: "http://"
// });

const xml = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:spy="spyne.examples.hello.soap"><soap:Header/><soap:Body><spy:getAllUsers/></soap:Body></soap:Envelope>';

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

var api = {

    users: {
        getAllUsers() {
            // const url = 'http://127.0.0.2:8000/?wsdl'
            // const args = { name: 'john' };

            // soap.createClientAsync(url).then((client) => {
            //     return client['getAllUsers']();
            // }).then((response) => {
            //     console.log(response)
            // }).catch((error) => {
            //     console.log(error)
            // });

            // soap.createClient(url, function(err, client) {
            //     client.getAllUsers(args, function(err, result) {
            //         console.log(result);
            //     })
            // })

            // ==============================================================

            // let testeXML = '<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:myap="myapp"><soapenv:Header><myap:MyHeader><!--Optional:--><myap:myinfo>?</myap:myinfo></myap:MyHeader></soapenv:Header><soapenv:Body><myap:MyMethod><!--Optional:--><myap:mymethodparam>?</myap:mymethodparam></myap:MyMethod></soapenv:Body></soapenv:Envelope>'

            axios.post('http://127.0.0.2:8000/?wsdl', xml, {
                headers: {
                    'Content-Type': 'application/xml',
                    'Access-Control-Allow-Origin': '*',
                    'Access-Control-Allow-Methods': '*'
                }
            }).then(res => console.log(res));

            //==============================================================

            // const url = 'http://127.0.0.2:8000/?wsdl';
            // const xhr = new XMLHttpRequest();
            // xhr.open("GET", url);

            // xhr.setRequestHeader("Content-Type", "application/text");
            // xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
            // xhr.setRequestHeader('Access-Control-Allow-Methods', '*');
            
            // xhr.onreadystatechange = function () {
            //     console.log(xhr.status);
            //     console.log(xhr.responseText);
            //     // if (xhr.readyState === 4) {
            //     //    console.log(xhr.status);
            //     //    console.log(xhr.responseText);
            //     // }
            // };

            // xhr.send(testeXML);

            // return users;
        },
        registerNewUser(newUser) {
            return users.push(newUser);
        }
    }

}

export default api;