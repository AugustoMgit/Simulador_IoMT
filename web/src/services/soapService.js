const parse = require('xml-js');

const url = 'http://127.0.0.2:8000/?wsdl';

var soapService = {
    
    users: {
        getAllUsers() {
            return new Promise((resolve, reject) => {
                const xml = '<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:spy="spyne.examples.hello.soap"><soap:Header/><soap:Body><spy:getAllUsers/></soap:Body></soap:Envelope>';
                const xhr = new XMLHttpRequest();
                xhr.open("POST", url, true);
    
                xhr.setRequestHeader("Content-Type", "application/xml");
                // xhr.setRequestHeader("Access-Control-Allow-Origin", "*");
                // xhr.setRequestHeader('Access-Control-Allow-Methods', '*');

                function extractUsers(value) {
                    let users = value['soap12env:Envelope']['soap12env:Body']['tns:getAllUsersResponse']['tns:getAllUsersResult']['tns:string'];
                    let array = [];
                    users.forEach(element => {
                        let user = {}
                        let data = element._text.replace('(', '').replace(')', '').replaceAll("'", "");
                        data = data.split(',')
                        user.id = data[0];
                        user.name = data[1];
                        user.birthday = data[2];
                        user.gender = data[3];
                        user.email = data[4];
                        array.push(user);
                    });
                    resolve(array);
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
            return new Promise((resolve, reject) => {
                const xml = `<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:spy="spyne.examples.hello.soap">
                <soap:Header/>
                <soap:Body>
                   <spy:addUser>
                      <!--Optional:-->
                      <spy:nome>${newUser.name}</spy:nome>
                      <!--Optional:-->
                      <spy:nascimento>${newUser.birthday}</spy:nascimento>
                      <!--Optional:-->
                      <spy:sexo>${newUser.gender}</spy:sexo>
                      <!--Optional:-->
                      <spy:email>${newUser.email}</spy:email>
                   </spy:addUser>
                </soap:Body>
             </soap:Envelope>`

                    const xhr = new XMLHttpRequest();
                    xhr.open("POST", url, true);
        
                    xhr.setRequestHeader("Content-Type", "application/xml");
        
                    xhr.onload = function () {
                        if (xhr.status === 200) {
                            resolve(xhr.response);
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
        deleteUser(id) {
            return new Promise((resolve, reject) => {
                const xml = `<soap:Envelope xmlns:soap="http://www.w3.org/2003/05/soap-envelope" xmlns:spy="spyne.examples.hello.soap">
                <soap:Header/>
                <soap:Body>
                   <spy:deleteUser>
                      <!--Optional:-->
                      <spy:id_user>${id}</spy:id_user>
                   </spy:deleteUser>
                </soap:Body>
             </soap:Envelope>`

                    const xhr = new XMLHttpRequest();
                    xhr.open("POST", url, true);
        
                    xhr.setRequestHeader("Content-Type", "application/xml");
        
                    xhr.onload = function () {
                        if (xhr.status === 200) {
                            resolve(xhr.response);
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
        }
    }

}

export default soapService;