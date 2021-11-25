<template>
  <div>
    <b-container>
      <b-row>
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

              </b-form-row>

              <b-form-row>
                <b-col>
                  <b-button type="submit" variant="primary" class="mr-2">Submit</b-button>
                  <b-button type="reset"  variant="secondary">Reset</b-button>
                </b-col>
              </b-form-row>

            </b-form>
          </b-card>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <b-card title="Users">
            <b-table striped bordered
              :items="allUsers">

            </b-table>
          </b-card>
        </b-col>
      </b-row>
    </b-container>
  </div>
</template>

<script>
import restApi from '@/services/restService'

export default {
  name: 'RegisterUser',

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
      restApi.users.registerNewUser(this.newUserForm);
      this.getAllUsers();
    },
    onReset() {
      console.log('form reset')
    },

    getAllUsers() {
      this.allUsers = restApi.users.getAllUsers();
    }

  },

  mounted() {
    this.getAllUsers();
  }

}
</script>

<style>

</style>