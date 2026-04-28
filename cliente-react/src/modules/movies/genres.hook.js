import { useEffect, useState } from "react";
import { 
    getGenres,
    createGenre,
    updateGenre,
    deleteGenre
} from "../../api/genres.api";

export const useGenres = () => {
    const [genres, setGenres] = useState([]);

    const fetchGenres = async () => {
        const res = await getGenres();
        setGenres(res.data);
    };

    useEffect(() => {
        fetchGenres();
    }, []);

    const save = async (form, selected) => {
        if (selected) {
            await updateGenre(selected.id, form);
        } else {
            await createGenre(form);
        }
        fetchGenres();
    };

    const remove = async (id) => {
        await deleteGenre(id);
        fetchGenres();
    };

    return {
        genres,
        save,
        remove,
    };
};