import { apiClient } from "./client";

export const getGenres = () => apiClient.get("/genres/");
export const getGenre = (id) => apiClient.get(`/genres/${id}/`);

export const createGenre = (data) => apiClient.post("/genres/", data);

export const updateGenre = (id, data) =>
    apiClient.put(`/genres/${id}/`, data);

export const deleteGenre = (id) =>
    apiClient.delete(`/genres/${id}/`);