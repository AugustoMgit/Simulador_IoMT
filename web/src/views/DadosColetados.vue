<template>
    <div>
        <b-row class="mb-2">
        <b-col>
            <b-card title="Dados coletados">
                <b-form @submit="onSubmit" @reset="onReset">
                    <b-form-row>
                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="Name:" label-for="input-user-name" >Username</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-name" v-model="newUserForm.name" type="text" placeholder="Enter name" required ></b-form-input>
                                </b-input-group>
                            </b-col>
                        </b-form-group>

                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="Tipo:" label-for="input-user-tipo" >Tipo</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-tipo" v-model="newUserForm.tipo" type="text" placeholder="Enter type" required ></b-form-input>
                                </b-input-group>
                            </b-col>
                        </b-form-group>

                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="Valor 1:" label-for="input-user-valor1" >Valor 1</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-name" v-model="newUserForm.valor1" type="text" placeholder="Enter valor 1" required ></b-form-input>
                                </b-input-group>
                            </b-col>
                        </b-form-group>

                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="Valor 2:" label-for="input-user-valor2" >Valor 2</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-valor2" v-model="newUserForm.valor2" type="text" placeholder="Enter valor 2" required ></b-form-input>
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
  name: 'DadosColetados',

  data() {
    return {

        newUserForm: {
        name: '',
        tipo: '',
        valor1: '',
        valor2: '',
      },

      allUsers: []
    }
  },

    methods: {
        onSubmit() {
        restService.restApi.dados(this.newUserForm);
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
