import axios from 'axios';
// import authHeader from './AuthHeader';


const API_URL = `${process.env.VUE_APP_API_ENDPOINT}`;

export default {
  getAll() {
    return axios.get(`${API_URL}/property/`);
  },
  searchByKeyword(keyword) {
    return axios.get(`${API_URL}/property/?search=${keyword}/`);
  },
  update(id, data) {
    return axios.put(`${API_URL}/property/${id}/`, data);
  },
};
