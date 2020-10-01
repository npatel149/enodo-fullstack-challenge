import Vue from 'vue';
import Vuex from 'vuex';
import getters from './getters';
import actions from './actions';
import mutations from './mutations';
import propertyinfo from './modules/propertyinfo.module';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {},
  getters,
  actions,
  mutations,
  modules: {
    propertyinfo,
  },
});
