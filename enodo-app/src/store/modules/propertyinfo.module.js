import PropertyInfoService from '@/services/PropertyInfoService';

export default {
  namespace: true,
  state: {
    search: '',
    propertyList: [],
    selectedPropertyList: [],
    suggestionsLinks: [],
    accessToken: localStorage.getItem('accessToken') || null,
    userId: 'npatel',
    loggedIn: true,
    user: JSON.parse(localStorage.getItem('user')) || null,
  },
  /* eslint-disable no-param-reassign */
  getters: {
    filteredList(state) {
      return state.propertyList.filter(property => {
        return property.full_address.toLowerCase().includes(state.search.toLowerCase())
      })
    },
    propertyList(state) {
      return state.propertyList;
    },
    suggestionsLinks(state) {
      // state.suggestionsLinks = state.propertyList.map(obj=> obj['value'] = obj['full_address']);
      let links = state.propertyList
      let i;
      for (i = 0; i < links.length; i++) {
        links[i]['value'] = links[i]['full_address'];
      }
      state.suggestionsLinks = links;
      return state.suggestionsLinks
    }
  },
  /* eslint-disable no-param-reassign */
  actions: {
    fetchPropertyList({commit}) {
      PropertyInfoService.getAll().then(
        (response) => {
          commit('STORE_PROPERTY_LIST_SUCCESS', response.data);
          return Promise.resolve(response.data);
        },
      ).catch(
        (error) => {
          commit('STORE_PROPERTY_LIST_FAILURE');
          return Promise.reject(error);
        },
      );
    },
    toggleIsSelected({commit}, propertyInfo) {
      console.log('step-1:  ', propertyInfo.is_selected );
      propertyInfo.is_selected = !propertyInfo.is_selected;
      console.log('step-2:  ', propertyInfo.is_selected );
      PropertyInfoService.update(propertyInfo.id, propertyInfo).then(
        (response) => {
          commit('TOGGLE_IS_SELECTED_SUCCESS', response.data);
          console.log('step-3:  ', propertyInfo.is_selected );
          if (propertyInfo.is_selected) {
            console.log('SELECTED_LIST_ADD_ELEMENT');
            commit('SELECTED_LIST_ADD_ELEMENT', response.data)
          } else {
            console.log('SELECTED_LIST_REMOVE_ELEMENT');
            commit('SELECTED_LIST_REMOVE_ELEMENT', response.data)
          }
        },
      ).catch(
        (error) => {
          commit('TOGGLE_IS_SELECTED_FAILURE');
          propertyInfo.is_selected = !propertyInfo.is_selected;
          return Promise.reject(error);
        },
      );
    },
  },
  /* eslint-disable no-param-reassign */
  mutations: {
    SEARCH_BY_KEYWORD(state, search) {
      state.search = search;
    },
    SELECTED_LIST_ADD_ELEMENT(state, propertyInfo) {
      state.selectedPropertyList.push(propertyInfo);
    },
    SELECTED_LIST_REMOVE_ELEMENT(state, propertyInfo) {
      const index = state.selectedPropertyList.findIndex(obj => obj.id === propertyInfo.id);
      if (index > -1) {
        state.selectedPropertyList.splice(index, 1);
      }
    },
    STORE_PROPERTY_LIST_SUCCESS(state, propertyData) {
      state.propertyList = propertyData;
      state.selectedPropertyList = state.propertyList.filter((property) => property.is_selected);
    },
    STORE_PROPERTY_LIST_FAILURE(state) {
      state.propertyList = [];
      state.selectedPropertyList = [];
      console.log('Failed, to fetch all properties!');
    },
    TOGGLE_IS_SELECTED_FAILURE() {
      console.log('TOGGLE_IS_SELECTED_FAILURE');
    },
    TOGGLE_IS_SELECTED_SUCCESS(state, propertyInfo) {
      const index = state.propertyList.findIndex(obj => obj.id === propertyInfo.id);
      if (index > -1) {
        state.propertyList[index].is_selected = propertyInfo.is_selected;
      }
      console.log('TOGGLE_IS_SELECTED_SUCCESS');
    },
  },
};
