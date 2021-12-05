<template>
  <div>
    <b-container>
      <b-row class="mb-2">
        <b-col>
          <b-card title="Register new User">
            <b-form @submit="onSubmit" @reset="onReset">
              <b-form-row>
                <b-col>
                  <b-form-group
                    label="Name:"
                    label-for="input-user-name">
                    <b-form-input
                      id="input-user-name"
                      v-model="newUserForm.name"
                      type="text"
                      placeholder="Enter name"
                      required
                    ></b-form-input>
                  </b-form-group>
                </b-col>

                <b-col>
                  <b-form-group
                    label="Birth date:"
                    label-for="input-user-birthdate">
                    <b-form-input
                      id="input-user-birthdate"
                      v-model="newUserForm.birthday"
                      type="date"
                      placeholder="Enter birthday"
                      required
                    ></b-form-input>
                  </b-form-group>
                </b-col>

                <b-col>
                  <b-form-group
                    label="Gender:"
                    label-for="input-user-gender" required>
                    <b-form-radio v-model="newUserForm.gender" value="M">Male</b-form-radio>
                    <b-form-radio v-model="newUserForm.gender" value="F">Female</b-form-radio>
                  </b-form-group>
                </b-col>

                <b-col>
                  <b-form-group
                    label="E-mail:"
                    label-for="input-user-email">
                    <b-form-input
                      id="input-user-email"
                      v-model="newUserForm.email"
                      type="email"
                      placeholder="Enter e-mail"
                      required
                    ></b-form-input>
                  </b-form-group>
                </b-col>

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
      <b-row>
        <b-col>
          <b-card title="Users">
            <!-- <b-list-group class="mb-4">
              <b-list-group-item v-for="user in allUsers" :key="user._text">{{ user._text }}</b-list-group-item>
            </b-list-group> -->
            <b-table striped bordered
              :items="allUsers" :fields="tableFields">
              
              <template #cell(actions)="row">
                <b-button-close @click="deleteUser(row.item.id)"></b-button-close>
              </template>

            </b-table>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import soapApi from '@/services/soapService'

export default {
  name: 'RegisterUser',

  data() {
    return {

      newUserForm: {
        name: '',
        birthday: '',
        gender: '',
        email: '',
      },

      allUsers: [],

      tableFields: [
        'name', 'birthday', 'gender', 'email',
        { key: 'actions', label: 'Actions' }
      ]

    }
  },

  methods: {
    onSubmit() {
      soapApi.users.registerNewUser(this.newUserForm)
      .then(() => {
        this.$bvModal.msgBoxOk('User registered successfully.')
      })
      .catch(error => {
        console.log(error);
        this.$bvModal.msgBoxOk('An unexpected error occurred!')
      })
      this.getAllUsers();
    },
    onReset() {
      console.log('form reset');
    },

    getAllUsers() {
      soapApi.users.getAllUsers()
      .then(users => {
        this.allUsers = users;
      })
      .catch(error => {
        console.log(error)
        this.$bvModal.msgBoxOk('An unexpected error occurred!')
      });
    },

    deleteUser(id) {
      this.$bvModal.msgBoxConfirm('Are you sure?')
      .then(isConfirmed => {
        if(isConfirmed) this.confirmDeleteUser(id);
      })
    },

    confirmDeleteUser(id) {
      soapApi.users.deleteUser(id)
      .then(() => {
        this.$bvModal.msgBoxOk('User deleted successfully')
      })
      .catch(error => {
        console.log(error);
        this.$bvModal.msgBoxOk('An unexpected error occurred!')
      });
      this.getAllUsers();
    }

  },

  mounted() {
    this.getAllUsers();
  }

}
</script>

<style>

</style>