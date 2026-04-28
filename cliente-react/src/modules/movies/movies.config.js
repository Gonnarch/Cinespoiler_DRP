export const moviesConfig = {
    title: "Gestión de Películas",
    entityName: "película",
    entityNamePlural: "películas",
    imageField: "image_url",

    fields: [
        { name: "title", label: "Titulo" },
        { name: "status", label: "Estado" },
        { name: "duration_minutes", label: "Duración" },
    ],

    formFields: [
        { name: "title", label: "Titulo" },
        { name: "description", label: "Descripción" },
        { name: "release_date", label: "Fecha de Estreno", type: "date" },
        { name: "duration_minutes", label: "Duración (min)", type: "number" },
        { name: "image_url", label: "URL de la Imagen", type: "url" },

        {
            name: "status",
            label: "Estado",
            type: "select",
            options: [
                { value: "draft", label: "Borrador" },
                { value: "published", label: "Publicado" },
                { value: "coming_soon", label: "Próximamente" },
                { value: "archived", label: "Archivado" },
            ],
        },

        {
            name: "genres",
            label: "Géneros",
            type: "multiselect",
            optionLabel: "name",
            optionValue: "id",
            endpoint: "/genres"
        }
    ],
};