<template>
    <div>
        <b-row class="mb-2">
        <b-col>
            <b-card title="Dados simulados">
                <b-form @submit="onSubmit" @reset="onReset">
                    <b-form-row>
                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="Usuarios:" label-for="input-user-name" > Usuarios</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-usuarios" v-model="newUserForm.usuarios" type="text" placeholder="Enter usuarios" required ></b-form-input>

                                    <template #append>
                                    <b-dropdown text="Dropdown" variant="success">
                                        <b-dropdown-item>Action A</b-dropdown-item>
                                        <b-dropdown-item>Action B</b-dropdown-item>
                                    </b-dropdown>
                                    </template>
                                </b-input-group>
                            </b-col>
                        </b-form-group>

                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="Tipos:" label-for="input-user-tipos" >Tipos</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-tipos" v-model="newUserForm.tipos" type="text" placeholder="Enter tipos" required ></b-form-input>

                                    <template #append>
                                    <b-dropdown text="Dropdown" variant="success">
                                        <b-dropdown-item>Action A</b-dropdown-item>
                                        <b-dropdown-item>Action B</b-dropdown-item>
                                    </b-dropdown>
                                    </template>
                                </b-input-group>
                            </b-col>
                        </b-form-group>

                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="Quantidade:" label-for="input-user-quantidade" >Quantidade</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-quantidade" v-model="newUserForm.quantidade" type="text" placeholder="Enter quantidade" required ></b-form-input>
                                </b-input-group>
                            </b-col>
                        </b-form-group>

                    </b-form-row>

                    <b-form-row>

                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="MinMinuto:" label-for="input-user-minminuto" >Min. Minutos</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-minminuto" v-model="newUserForm.minminuto" type="text" placeholder="Enter min minuto" required ></b-form-input>
                                </b-input-group>
                            </b-col>
                        </b-form-group>

                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="MaxMinuto:" label-for="input-user-maxminuto" >Max. Minutos</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-maxminuto" v-model="newUserForm.maxminuto" type="text" placeholder="Enter max minuto" required ></b-form-input>
                                </b-input-group>
                            </b-col>
                        </b-form-group>
                    </b-form-row>

                    <b-form-row>
                        <b-col>
                            <div class="ml-auto">
                                <b-button type="submit" variant="primary" class="mr-2">Submit</b-button>
                                <b-button type="reset"  variant="secondary">Reset</b-button>
                            </div>
                        </b-col>
                    </b-form-row>
                </b-form>
            </b-card>
        </b-col>
    </b-row>
    </div>    
</template>
<script>
import restService from '@/services/restService'

export default {
  name: 'Simulador',

  data() {
    return {

        newUserForm: {
        usuarios: '',
        tipos: '',
        quantidade: '',
        minminuto: '',
        maxminuto: '',
      },

      allUsers: []
    }
  },

    methods: {
        onSubmit() {
        restService.restApi.simulador(this.newUserForm);
        this.getAllUsers();
        },
        onReset() {
        console.log('form reset')
        },

        getAllUsers() {
        //this.allUsers = restApi.users.getAllUsers();
        }
  },

  mounted() {
    this.getAllUsers();
  }

}
</script>
