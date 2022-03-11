FROM node:16-alpine as staging
ENV NODE_ENV staging

WORKDIR /my-app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 3000

CMD ["npm","start"]

FROM node:16-alpine AS builder
ENV NODE_ENV production
# Add a work directory
WORKDIR /my-app
# Cache and Install dependencies
COPY package*.json ./
# Copy app files
COPY . .
# Build the app
RUN npm run build

FROM nginx:1.21.0-alpine as production
ENV NODE_ENV production
COPY --from=builder /my-app/build /usr/share/nginx/html
COPY nginx.conf /etc/nginx/conf.d/default.conf

EXPOSE 80
# Start nginx
CMD ["nginx", "-g", "daemon off;"]