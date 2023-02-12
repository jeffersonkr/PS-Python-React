import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class ProductService {

    constructor() { }

    getProducts() {
        const url = `${API_URL}/product/`;
        return axios.get(url);
    }
}
