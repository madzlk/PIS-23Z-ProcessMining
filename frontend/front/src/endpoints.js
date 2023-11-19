const api_url = process.env.API_URL
    ? process.env.API_URL
    : "http://localhost:8080";

console.log("API_URL:", api_url);

export const get_all_users_by_id_endpoint = `${api_url}/users`;
