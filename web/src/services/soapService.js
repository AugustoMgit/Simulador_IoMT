const parse = require('xml-js');
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

var soapService = {
    
    users: {
        getAllUsers() {
            return new Promise((resolve, reject) => {
                const xml = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:spy="spyne.examples.hello.soap"><soap:Header/><soap:Body><spy:getAllUsers/></soap:Body></soap:Envelope>';
                const url = 'http://127.0.0.2:8000/?wsdl';
                const xhr = new XMLHttpRequest();
                xhr.open("POST", url, true);
    
                xhr.setRequestHeader("Content-Type", "application/xml");
                // xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
                // xhr.setRequestHeader('Access-Control-Allow-Methods', '*');

                function extractUsers(value) {
                    resolve(value['soap12env:Envelope']['soap12env:Body']['tns:getAllUsersResponse']['tns:getAllUsersResult']['tns:string']);
                    // let array = [];
                    // users.forEach(element => {
                    //     array.push(element._text)
                    // });
                    // resolve(array);
                }
    
                xhr.onload = function () {
                    if (xhr.status === 200) {
                        extractUsers(parse.xml2js(xhr.response, {compact: true, spaces: 4}));
                    } else {
                        reject({
                            status: xhr.status,
                            statusText: xhr.statusText
                        })
                    }
                };
                xhr.onerror = function () {
                    reject({
                        status: this.status,
                        statusText: xhr.statusText
                    });
                };
                
                xhr.send(xml);
            })
        },
        registerNewUser(newUser) {
            return users.push(newUser);
        }
    }

}

export default soapService;