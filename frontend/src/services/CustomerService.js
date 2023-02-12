import axios from 'axios';
const API_URL = 'http://localhost:8000';

export default class CustomerService {

    constructor() { }

    createCustomer(customer) {
        const url = `${API_URL}/account/register/`;
        return axios.post(url, customer);
    }
    updateCustomerPassword(customer) {
        const url = `${API_URL}/account/change_password/${customer.pk}`;
        return axios.patch(url, customer);
    }
    updateCustomer(customer) {
        const url = `${API_URL}/account/update_profile/${customer.pk}`;
        return axios.patch(url, customer);
    }
}
