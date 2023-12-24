import { defineConfig, loadEnv } from "vite";
import react from "@vitejs/plugin-react";
import ImportMetaEnvPlugin from "@import-meta-env/unplugin";

// Load environment variables
const env = loadEnv(process.env.MODE, process.cwd());

export default defineConfig(({ command, mode }) => {
  return {
    plugins: [react()],
    server: {
      host: true,
      port: 8000, // This is the port which we will use in docker
      // Thanks @sergiomoura for the window fix
      // add the next lines if you're using windows and hot reload doesn't work
      watch: {
        usePolling: true,
      },
    },

    // Additional Vite configuration...

    define: {
      // Pass environment variables to the application
      "process.env": Object.assign({}, env),
    },
  };
});

// You can use the 'env' variable outside of the 'defineConfig' block
console.log(env);
