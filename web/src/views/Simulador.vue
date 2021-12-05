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
                                        <b-input-group-text label="Name:" label-for="input-user-name" > Usuarios</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-name" v-model="newUserForm.name" type="text" placeholder="Enter name" required ></b-form-input>

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
                                        <b-input-group-text label="Name:" label-for="input-user-name" >Tipos</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-name" v-model="newUserForm.name" type="text" placeholder="Enter name" required ></b-form-input>

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
                                        <b-input-group-text label="Name:" label-for="input-user-name" >Quantidade</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-name" v-model="newUserForm.name" type="text" placeholder="Enter name" required ></b-form-input>
                                </b-input-group>
                            </b-col>
                        </b-form-group>

                    </b-form-row>

                    <b-form-row>

                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="Name:" label-for="input-user-name" >Min. Minutos</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-name" v-model="newUserForm.name" type="text" placeholder="Enter name" required ></b-form-input>
                                </b-input-group>
                            </b-col>
                        </b-form-group>

                        <b-form-group>
                            <b-col>
                                <b-input-group>
                                    <template #prepend>
                                        <b-input-group-text label="Name:" label-for="input-user-name" >Max. Minutos</b-input-group-text>
                                    </template>
                                    <b-form-input id="input-user-name" v-model="newUserForm.name" type="text" placeholder="Enter name" required ></b-form-input>
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

export default {
  name: 'Simulador',

  data() {
    return {

        newUserForm: {
        name: '',
        birthday: '',
        gender: '',
      },

      allUsers: []
    }
  },

    methods: {
        onSubmit() {
        //restApi.users.registerNewUser(this.newUserForm);
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
