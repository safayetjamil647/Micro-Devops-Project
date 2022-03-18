FROM node:16-alpine as dev
ENV NODE_ENV dev

WORKDIR /my-app

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm","start"]

FROM node:16-alpine AS builder
ENV NODE_ENV production
# Add a work directory
WORKDIR /my-app
# Cache and Install dependencies
COPY package*.json ./

RUN npm i react-scripts

# Copy app files
COPY . .
# Build the app
RUN npm run build

FROM nginx:1.21.0-alpine as production
ENV NODE_ENV production
COPY --from=builder /my-app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf
# Start nginx
CMD ["nginx", "-g", "daemon off;"]